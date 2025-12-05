def find_gaps(road):
    """
    Finds continuous empty segments (0's) in a road.
    Returns list of tuples: (start_index, length), sorted by longest first.
    """
    gaps = []
    start = None

    for i, val in enumerate(road):
        if val == 0 and start is None:
            start = i
        elif val == 1 and start is not None:
            gaps.append((start, i - start))
            start = None

    if start is not None:
        gaps.append((start, len(road) - start))

    return sorted(gaps, key=lambda x: x[1], reverse=True)

