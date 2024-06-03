def min_dist(A: list[int]) -> tuple[int, int] | None:
    
    if not A:
        return None
    
    # Sort the array
    A = sorted(A)

    # Initial values
    min_ = float("inf")
    val1 = None
    val2 = None

    # Iterate through the array
    for i in range(len(A) - 1):
        diff = abs(A[i] - A[i + 1])
        # If the current difference is smaller
        # change values
        if diff < min_:
            min_ = diff
            val1 = A[i]
            val2 = A[i + 1]

    return val1, val2