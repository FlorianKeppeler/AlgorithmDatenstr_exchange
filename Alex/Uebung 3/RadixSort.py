"""
Bucketsort implementation using linked lists

Copyright 2020, University of Freiburg.

Philipp Schneider <philipp.schneider@cs.uni-freiburg.de>
"""

import math  # noqa
import random
import time

from BucketSort import bucket_sort


def radix_sort(array: list, k: int) -> None:
    """
    Implements the radix sort algorithm to sort
        data elements with keys in range(k+1)

    Args:
        array: array of data elements
        k: largest key

    >>> array = [10-i for i in range(10)]
    >>> radix_sort(array, 100)
    >>> str(array)
    '[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]'
    """

    # k can't be negative
    if k < 0:
        raise ValueError("Error: k should be a postitive integer.")

    # if arrays if empty
    if not array:
        return

    # base and amount of digits
    b = 10
    m = math.ceil(math.log(k, b))

    # apply bucket sort with modified key function
    # to sort by digit
    for i in range(m):
        bucket_sort(array, b, lambda number: number % 10 ** (i + 1) // 10**i)


def is_sorted(lst):
    """
    Method that checks whether or not a list is sorted

    Args:
        lst: the list that will be checked
    Returns:
    bool:    True if the list is sorted, false otherwise.
    """
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))


def radix_sort_performance(
    array_size: int, k_values_start: int, k_values_end: int, k_values_step: int
) -> dict:
    """
    Method that outputs key range and elapsed time for sorting.
    """

    points = dict()

    print(f"\nRADIX SORT\n")

    for k in range(k_values_start, k_values_end, k_values_step):
        array = [random.randint(0, k) for _ in range(array_size)]

        start_time = time.time()
        radix_sort(array, k)
        run_time = time.time() - start_time

        is_srtd = is_sorted(array)
        print(
            f"|     time: {run_time:<25}",
            f"|     k: {k:<10}",
            f"|     {is_srtd=}      |",
        )

        points[k] = run_time

    return points
