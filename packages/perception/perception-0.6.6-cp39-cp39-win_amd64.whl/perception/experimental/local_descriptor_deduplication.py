# pylint: disable=no-member,invalid-name,too-many-locals,too-many-arguments,too-many-return-statements
import typing
import logging
import concurrent.futures

import typing_extensions
import numpy as np
import pandas as pd
import tqdm
import cv2

import perception.hashers.tools as pht
import perception.experimental.approximate_deduplication as ad

LOGGER = logging.getLogger(__name__)
DEFAULT_MAX_FEATURES = 256
DEFAULT_THRESHOLD = 100
DEFAULT_COARSE_THRESHOLD = 75
DEFAULT_OVERLAP = 0.01
DEFAULT_MATCH_PCT = 0.4
DEFAULT_INTERSECTION = 0.6
DEFAULT_INLIERS = 5
DEFAULT_MAX_SIZE = 256
DEFAULT_MIN_FEATURES = 10
DEFAULT_RATIO = 0.5


MatchStats = typing_extensions.TypedDict(
    "MatchStats",
    {
        "match": typing.Optional[float],
        "good_A2B": typing.Optional[typing.List[bool]],
        "good_B2A": typing.Optional[typing.List[bool]],
        "min_kpBM": typing.Optional[int],
        "MAB": typing.Optional[str],
        "intersection": typing.Optional[float],
        "inliers": typing.Optional[float],
        "bounds_intersection": typing.Optional[float],
    },
)


def load_and_preprocess(filepath, max_size=DEFAULT_MAX_SIZE, grayscale=True):
    """Read, unletterbox, and resize an image.

    Args:
        filepath: The path to the file
        max_size: The maximum size for a dimension of the image
        grayscale: Set to false to get RGB
    """
    image = pht.read(filepath)
    if image is None:
        LOGGER.warning("Failed to load image %s", filepath)
        return None
    res = pht.unletterbox(image)
    if res is None:
        return None
    (x1, x2), (y1, y2) = res
    image = np.ascontiguousarray(image[y1:y2, x1:x2])
    if grayscale:
        image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    max_dimension = max(image.shape[:2])
    if max_dimension > max_size:
        scale = max_size / max_dimension
        image = cv2.resize(
            image, (int(image.shape[1] * scale), int(image.shape[0] * scale))
        )
    return image


def generate_image_descriptors(
    filepath: str,
    max_features=DEFAULT_MAX_FEATURES,
    min_features=DEFAULT_MIN_FEATURES,
    max_size=DEFAULT_MAX_SIZE,
) -> typing.Optional[typing.Tuple[np.ndarray, np.ndarray, typing.Tuple[int, int]]]:
    """Generate SIFT descriptors for a file.

    Args:
        filepath: Path to image file.
        max_features: The maximum number of features to
            extract.
        min_features: The minimum number of features to
            extract.
        max_size: The maximum side length for an image.

    Returns:
        If successful, returns a tuple of keypoints, descriptors,
        and a (width, height) tuple.
    """
    sift = cv2.SIFT_create(nfeatures=max_features)
    try:
        image = load_and_preprocess(filepath, max_size=max_size)
        if image is None:
            return None
        keypoints, descriptors = sift.detectAndCompute(image, None)
    except FileNotFoundError:
        LOGGER.warning("Image file %s not found.", filepath)
        return None
    except ValueError as e:
        LOGGER.error("Processing image file %s failed.", filepath, exc_info=e)
        return None

    if descriptors is None:
        return None
    if descriptors.shape[0] < min_features:
        return None
    keypoints = np.array([kp.pt for kp in keypoints], dtype=np.float32)
    return keypoints, descriptors, (image.shape[1], image.shape[0])


def build_reference_df(
    filepaths: typing.Iterable[str],
    max_features=DEFAULT_MAX_FEATURES,
    min_features=DEFAULT_MIN_FEATURES,
    max_size=DEFAULT_MAX_SIZE,
) -> pd.DataFrame:
    """Build SIFT descriptors for a list of files.

    Args:
        filepaths: A list of filepaths for which descriptors
            are desired.
        max_features: The maximum number of features to
            extract.
        min_features: The minimum number of features to
            extract.
        max_size: The maximum side length for an image.

    Returns:
        A dataframe, indexed by filepath with columns for descriptors
        and descriptor counts.
    """
    LOGGER.debug("Generating descriptors")
    features = [
        generate_image_descriptors(
            filepath,
            max_features=max_features,
            min_features=min_features,
            max_size=max_size,
        )
        for filepath in filepaths
    ]
    LOGGER.debug("Finished computing descriptors.")
    return pd.DataFrame(
        {
            "descriptors": [f[1] if f is not None else None for f in features],
            "keypoints": [f[0] if f is not None else None for f in features],
            "descriptor_count": [
                f[1].shape[0] if f is not None else None for f in features
            ],  # type: ignore
            "dimensions": [f[2] if f is not None else None for f in features],
            "filepath": filepaths,
        }
    ).set_index("filepath")


def compute_pairs(
    match_df,
    query_df=None,
    threshold=DEFAULT_THRESHOLD,
    minimum_overlap=DEFAULT_OVERLAP,
    pct_probe=0.1,
    use_gpu: bool = True,
    faiss_cache_path: str = None,
):
    """Compute pairs of matching images from a reference
    dataframe.
    Args:
        match_df: A dataframe, as computed by build_reference_df, will compute pairs against self,
            unless query_df is provided.
        query_df: optional, if provided will be used to query against match_df for matches.
        threshold: The match threshold between two vectors.
        minimum_overlap: The minimum overlap between a pair of files.
        pct_probe: The percentage of the dataset to search for approximate
            search.
        faiss_cache_path: If provided load any existing faiss index from this path, and if
            it does not exist then save the generated faiss index to the path.
    """
    match_df = match_df.dropna(subset=["descriptors"])
    counts = match_df["descriptor_count"].values.astype("uint32")
    descriptors = np.vstack(match_df["descriptors"].values)

    if query_df is None:
        y_counts = None
        y_descriptors = None
    else:
        query_df = query_df.dropna(subset=["descriptors"])
        y_counts = query_df["descriptor_count"].values.astype("uint32")
        y_descriptors = np.vstack(query_df["descriptors"].values).astype("float32")

    pairs = ad.compute_euclidean_pairwise_duplicates_approx(
        X=descriptors.astype("float32"),
        counts=counts,
        threshold=threshold,
        minimum_overlap=minimum_overlap,
        pct_probe=pct_probe,
        Y=y_descriptors,
        y_counts=y_counts,
        use_gpu=use_gpu,
        faiss_cache_path=faiss_cache_path,
    )

    if query_df is None:
        query_df = match_df  # Assign query_df to be able to lookup matches.

    return [(query_df.iloc[p1].name, match_df.iloc[p2].name) for p1, p2 in pairs]


def compute_area(box):
    """Compute the area of a box given a set
    of points x1, y1, x2, y2.

    Args:
        box: A list of coordinates.
    """
    return (box[3] - box[1]) * (box[2] - box[0])


def compute_intersection(kps, filter_arr):
    """Compute the percentage of area covered by
    a set of filtered keypoints versus raw keypoints.

    Args:
        kps: A list of points
        filter_arr: A filter array of same length as kps_raw
            indicating whether to keep that keypoint.
    """
    kps_filtered = kps[filter_arr]
    box_after = np.hstack([kps_filtered.min(axis=0), kps_filtered.max(axis=0)])
    box_before = np.hstack([kps.min(axis=0), kps.max(axis=0)])
    area_before = compute_area(box_before)
    area_after = compute_area(box_after)
    return area_after / area_before


def compute_minimum_intersection(kp1, kp2, filter_arr1, filter_arr2):
    """Compute the minimum intersection between two pairs
    of keypoints (filtered and unfiltered).

    Args:
        kp1: A list of the first set of keypoints
        kp2: A list of the second set of keypoints
        filter_arr1: A filter array for the first set of keypoints
        filter_arr2: A filter array for the second set of keypoints
    """
    return min(
        compute_intersection(kp1, filter_arr1), compute_intersection(kp2, filter_arr2)
    )


def validate_match(**kwargs) -> bool:
    """See validate_match_verbose.

    This exists to be backwards compatible, but no real reason to not migrate to
    just using `validate_match_verbose`
    """
    return validate_match_verbose(**kwargs)[0]


def validate_match_verbose(
    kp1: np.ndarray,
    des1: np.ndarray,
    kp2: np.ndarray,
    des2: np.ndarray,
    dims1: typing.Tuple[int, int],
    dims2: typing.Tuple[int, int],
    minimum_match: float = DEFAULT_MATCH_PCT,
    minimum_intersection: float = DEFAULT_INTERSECTION,
    minimum_inliers: int = DEFAULT_INLIERS,
    ratio=DEFAULT_RATIO,
) -> typing.Tuple[bool, MatchStats]:
    """Validate the match between two sets of keypoints and descriptors. The
    validation algorithm is as follows:

    #. Compute the mutual set of matches between the two sets of descriptors
       and filter them using Lowe's ratio test.
    #. If the minimum number of passing matches is less than "minimum_match",
       the match fails. This ensures we don't have trivial matches.
    #. Compute the intersection area of the matched keypoints versus the
       raw keypoints. If the area overlap is less than minimum_intersection,
       the match fails. This ensures we don't match on small subsegments of
       an image, such as logos.
    #. Compute a transformation matrix using cv2.findHomography. If we cannot
       obtain a transformation matrix, the match fails. If the sum total
       of inliers for the transformation matrix is less than minimum_inliers,
       the match fails.
    #. Finally, use the transformation matrix on a set of points representing
       the bounding box of each image. If less than minimum_intersection of
       the bounding box fits within the bounds of the transformed version,
       the match fails. This is a second pass safety check for logos and other
       subsegments of images.

    Args:
        kp1: The first set of keypoints
        des1: The first set of descriptors
        kp2: The second set of keypoints
        des2: The second set of descriptors
        dims1: The dimensions (width, height) for the first image
        dims2: The dimensions (width, height) for the second image
        minimum_match: The minimum number of matches passing the ratio test.
        minimum_intersection: The minimum overlapping area between the keypoints
            in the filtered set of matches and the original keypoints.
        minimum_inliers: The minimum number of inliers for the transformation
            matrix.
        ratio: The ratio to use for Lowe's ratio test.

    Returns:
        True if the match passes, False otherwise.
    """
    swap = kp1.shape[0] < kp2.shape[0]
    kpA = kp2 if swap else kp1
    kpB = kp1 if swap else kp2
    dimsA = dims2 if swap else dims1
    dimsB = dims1 if swap else dims2
    desA = des2 if swap else des1
    desB = des1 if swap else des2

    stats: MatchStats = {
        "match": None,
        "good_A2B": None,
        "good_B2A": None,
        "min_kpBM": None,
        "MAB": None,
        "intersection": None,
        "inliers": None,
        "bounds_intersection": None,
    }

    indexA = ad.build_index(desA, approximate=False)
    indexB = ad.build_index(desB, approximate=False)
    if desA is None or indexA is None or desB is None or indexB is None:
        return False, stats

    # pylint: disable=no-value-for-parameter
    distances_A2B, indexes_A2B = indexB.search(desA.astype("float32"), 2)
    distances_B2A, _ = indexA.search(desB.astype("float32"), 2)
    good_A2B, good_B2A = map(
        lambda distances: (distances[:, 0] < distances[:, 1] * ratio),
        [distances_A2B, distances_B2A],
    )
    match = min(good_A2B.sum() / good_A2B.shape[0], good_B2A.sum() / good_B2A.shape[0])
    stats["match"] = match

    # Can use these to filter which points match and filter points out if they match logos.
    if swap:
        stats["good_A2B"] = good_B2A
        stats["good_B2A"] = good_A2B
    else:
        stats["good_A2B"] = good_A2B
        stats["good_B2A"] = good_B2A

    if match < minimum_match:
        # We didn't get enough good matches.
        return False, stats
    kpAM = kpA[good_A2B]
    kpBM = kpB[indexes_A2B[good_A2B, 0]]

    # findHomography requires 4 points from each to work.
    stats["min_kpBM"] = min(len(kpAM), len(kpBM))
    if len(kpAM) < 4 or len(kpBM) < 4:
        return False, stats

    intersection = compute_minimum_intersection(
        kp1=kpA, kp2=kpB, filter_arr1=good_A2B, filter_arr2=indexes_A2B[good_A2B, 0]
    )
    stats["intersection"] = intersection
    if intersection < minimum_intersection:
        return False, stats

    MAB, mask = cv2.findHomography(
        kpAM.reshape(-1, 1, 2),
        kpBM.reshape(-1, 1, 2),
        cv2.RANSAC,
        1.0,
        maxIters=50_000,
        confidence=0.9999,
    )
    stats["MAB"] = "good"
    if MAB is None:
        # We didn't get a transformation matrix.
        stats["MAB"] = "is-None"
        return False, stats
    stats["inliers"] = mask.sum()
    if mask.sum() < minimum_inliers:
        # The transformation matrix didn't include enough inliers.
        return False, stats
    # Check how much of each original bounding box fits onto
    # the other image.
    try:
        MBA = np.linalg.inv(MAB)
    except np.linalg.LinAlgError:
        # We couldn't compute the matrix inverse.
        stats["MAB"] = "inverse-failed"
        return False, stats
    ptsA = np.array([[0, 0], dimsA]).astype("float32")
    ptsB = np.array([[0, 0], dimsB]).astype("float32")
    ptsAt = (
        cv2.perspectiveTransform(ptsA.reshape((-1, 1, 2)), MAB)
        .reshape(-1, 2)
        .clip(0, dimsB)
    )
    ptsBt = (
        cv2.perspectiveTransform(ptsB.reshape((-1, 1, 2)), MBA)
        .reshape(-1, 2)
        .clip(0, dimsA)
    )
    bounds_intersection = min(
        abs(np.prod(ptsBt[1] - ptsBt[0]) / np.prod(dimsA)),
        abs(np.prod(ptsAt[1] - ptsAt[0]) / np.prod(dimsB)),
    )
    stats["bounds_intersection"] = bounds_intersection
    if bounds_intersection < minimum_intersection:
        return False, stats
    return True, stats


def deduplicate_sift_dfs(
    match_df: pd.DataFrame,
    query_df: typing.Optional[pd.DataFrame] = None,
    coarse_pct_probe: float = ad.DEFAULT_PCT_PROBE,
    coarse_threshold: int = DEFAULT_COARSE_THRESHOLD,
    minimum_coarse_overlap: float = DEFAULT_OVERLAP,
    minimum_validation_match: float = DEFAULT_MATCH_PCT,
    minimum_validation_intersection: float = DEFAULT_INTERSECTION,
    minimum_validation_inliers: int = DEFAULT_INLIERS,
    ratio: float = DEFAULT_RATIO,
    max_workers: int = None,
    use_gpu: bool = True,
    faiss_cache_path: str = None,
    verbose: bool = False,
) -> typing.Union[
    typing.List[typing.Tuple[typing.Any, typing.Any]],
    typing.List[typing.Tuple[typing.Any, typing.Any, MatchStats]],
]:
    """Deduplicate images within one set of images or between two sets of images:
    #. Given a dataframe (or two) of SIFT descriptors and keypoints for images.
    #. Perform a coarse, approximate search for images with common features.
    #. For each candidate pair, validate it pairwise by checking the features
    and keypoints with the traditional approach using the ratio test. See
    validate_match for more information.
    Args:
        match_df: Dataframe of sift features to dedup within.
        query_df: If provided will search for matches between this and match_df, if None will
            just search match_df against itself.
        coarse_pct_probe: The minimum fraction of nearest lists to search. If
            the product of pct_probe and the number of lists is less
            than 1, one list will be searched.
        corase_threshold: The threshold for a match as a euclidean distance.
        minimum_coarse_overlap: The minimum overlap between two files to qualify as a match.
        minimum_validation_match: The minimum number of matches passing the ratio test.
        minimum_validation_intersection: The minimum overlapping area between the keypoints
            in the filtered set of matches and the original keypoints.
        minimum_validation_inliers: The minimum number of inliers for the transformation
            matrix.
        ratio: The ratio to use for Lowe's ratio test.
        max_workers: The maximum number of threads to use for doing the final validation
            step.
        faiss_cache_path: If provided load any existing faiss index from this path, and if
            it does not exist then save the generated faiss index to the path. Most helpful if
            doing multiple queries against the same match_df.
        verbose: return metada with matches such as overlap percent etc.
    Returns:
        A list of pairs of file duplicates.
        If verbose is true the tuple will be: (match_id1, match_id2, metadata_dict)
    """
    candidates = compute_pairs(
        match_df,
        query_df,
        pct_probe=coarse_pct_probe,
        threshold=coarse_threshold,
        minimum_overlap=minimum_coarse_overlap,
        use_gpu=use_gpu,
        faiss_cache_path=faiss_cache_path,
    )

    if query_df is None:
        reference_df = match_df
    else:
        candidate_filepath_set = set()
        for c1, c2 in candidates:
            candidate_filepath_set.add(c1)
            candidate_filepath_set.add(c2)

        # May not be necessary if c1 and c2 are always in the same set
        reference_df = pd.concat(
            [
                query_df[query_df.index.isin(candidate_filepath_set)],
                match_df[match_df.index.isin(candidate_filepath_set)],
            ]
        )

    keep: typing.Union[
        typing.List[typing.Tuple[typing.Any, typing.Any]],
        typing.List[typing.Tuple[typing.Any, typing.Any, MatchStats]],
    ] = []  # type: ignore
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        batch_size = 10_000
        for start in tqdm.tqdm(range(0, len(candidates), batch_size)):
            futures = {
                executor.submit(
                    validate_match_verbose,
                    des1=reference_df.loc[c1]["descriptors"],
                    kp1=reference_df.loc[c1]["keypoints"],
                    des2=reference_df.loc[c2]["descriptors"],
                    kp2=reference_df.loc[c2]["keypoints"],
                    dims1=reference_df.loc[c1]["dimensions"],
                    dims2=reference_df.loc[c2]["dimensions"],
                    minimum_match=minimum_validation_match,
                    minimum_inliers=minimum_validation_inliers,
                    minimum_intersection=minimum_validation_intersection,
                    ratio=ratio,
                ): (c1, c2)
                for c1, c2 in candidates[start : start + batch_size]
            }
            for future in concurrent.futures.as_completed(futures):
                is_match, metadata = future.result()
                if is_match:
                    if verbose:
                        keep.append(
                            (futures[future][0], futures[future][1], metadata)  # type: ignore
                        )
                    else:
                        keep.append(futures[future])  # type: ignore
    return keep


def deduplicate(
    filepaths_or_reference_df: typing.Union[typing.Iterable[str], pd.DataFrame],
    query_filepaths_or_df: typing.Optional[
        typing.Union[typing.Iterable[str], pd.DataFrame]
    ] = None,
    max_features: int = DEFAULT_MAX_FEATURES,
    min_features: int = DEFAULT_MIN_FEATURES,
    max_size: int = DEFAULT_MAX_SIZE,
    **kwargs,
) -> typing.Union[
    typing.List[typing.Tuple[typing.Any, typing.Any]],
    typing.List[typing.Tuple[typing.Any, typing.Any, MatchStats]],
]:
    """Deduplicate images by doing the following:
    #. Unletterbox all images and resize to some maximum size, preserving
       aspect ratio.
    #. Compute the SIFT descriptors and keypoints for all the resulting images.
    #. See `deduplicate_sift_dfs` for remaining steps.
    Args:
        filepaths_or_reference_df: The list of images to deduplicate, or a precomputed
            SIFT DataFrame.
        query_filepaths_or_df: If provided will look for matches between these files and
            the files in the first param.
        max_features: The maximum number of features to
            extract.
        min_features: The minimum number of features to
            extract.
        max_size: The maximum side length for an image.
    Returns:
        A list of pairs of file duplicates.
        If verbose is true the tuple will be: (match_id1, match_id2, metadata_dict)
    """
    if isinstance(filepaths_or_reference_df, pd.DataFrame):
        reference_df = filepaths_or_reference_df
    else:
        reference_df = build_reference_df(
            filepaths=filepaths_or_reference_df,
            max_features=max_features,
            min_features=min_features,
            max_size=max_size,
        )

    if query_filepaths_or_df is None:
        query_df = None
    else:
        if isinstance(query_filepaths_or_df, pd.DataFrame):
            query_df = query_filepaths_or_df
        else:
            query_df = build_reference_df(
                filepaths=query_filepaths_or_df,
                max_features=max_features,
                min_features=min_features,
                max_size=max_size,
            )

    return deduplicate_sift_dfs(reference_df, query_df=query_df, **kwargs)
