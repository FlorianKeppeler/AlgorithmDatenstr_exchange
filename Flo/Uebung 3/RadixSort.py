"""
Bucketsort implementation using linked lists

Copyright 2020, University of Freiburg.

Philipp Schneider <philipp.schneider@cs.uni-freiburg.de>
"""

from math import log10, ceil
import random
import time

from BucketSort import bucket_sort


def radix_sort(array: list[int], k: int) -> None:
    '''
    Implements the radix sort algorithm to sort
        data elements with keys in range(k+1)

    Args:
        array: array of data elements
        k: largest key

    >>> array = [10-i for i in range(10)]
    >>> radix_sort(array, 100)
    >>> str(array)
    '[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]'
    '''

    m = ceil(log10(k))

    for i in range(m):
        bucket_sort(array, 10, lambda x: x % 10**(i + 1) // 10**i)


def is_sorted(lst):
    """
        Method that checks whether or not a list is sorted

        Args:
            lst: the list that will be checked
        Returns:
        bool:    True if the list is sorted, false otherwise.
        """
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))


def radix_sort_performance():
    '''
    Method that outputs key range and elapsed time for sorting.
    '''
    tmp = dict()

    for k in range(2 * 10**4, (12 * (10**5)) + 1, 2 * 10**4):
        array = [random.randint(0, k) for i in range(10**4)]
        start_time = time.time()
        radix_sort(array, k)
        run_time = (time.time() - start_time) * 1000
        if not is_sorted(array):
            raise Exception("list not sorted successfully")
        print("%d\t%.1f" % (k, run_time))
        tmp[k] = run_time

    return tmp


if __name__ == "__main__":
    radix_sort_performance()
