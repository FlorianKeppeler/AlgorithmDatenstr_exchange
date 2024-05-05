"""
Bucketsort implementation using linked lists

Copyright 2020, University of Freiburg.

Philipp Schneider <philipp.schneider@cs.uni-freiburg.de>
"""

import random
import time

from Queue import Queue  # noqa
from ListElement import ListElement  # noqa


def bucket_sort(array: list, k, key=lambda x: x) -> None:
    """
    Implements the bucket sort algorithm to sort
        data elements using a key function to
        assign sorting keys to data elements

    Args:
        array: array of data elements
        k: largest key
        key: a function mapping data elements to values
        in range(k+1) (idendity function as default)

    >>> array = [10-i for i in range(10)]
    >>> bucket_sort(array, 10)
    >>> str(array)
    '[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]'
    """

    # k can't be negative
    if k < 0:
        raise ValueError("Error: k should be a postitive integer.")

    # If array is empty
    if not array:
        return

    # Create lists
    queues_list = [Queue() for _ in range(k + 1)]

    # Put elements with the same key
    # inside the queue as ListElement
    for item in array:
        queues_list[key(item)].enqueue(ListElement(item))

    index = 0

    # Pop each queue
    for q in queues_list:
        while not q.is_empty():
            # (because we know that current q isn't empty)
            array[index] = q.dequeue().get_key()  # type: ignore
            index += 1


def bucket_sort_performance(
    array_size: int, k_values_start: int, k_values_end: int, k_values_step: int
) -> dict:
    """
    Method that outputs key range and elapsed time for sorting.
    """

    points = dict()
    print(f"\nBUCKET SORT\n")
    for k in range(k_values_start, k_values_end, k_values_step):
        array = [random.randint(0, k) for _ in range(array_size)]

        start_time = time.time()
        bucket_sort(array, k)
        run_time = time.time() - start_time

        is_srtd = is_sorted(array)

        print(
            f"|     time: {run_time:<25}",
            f"|     k: {k:<10}",
            f"|     {is_srtd=}      |",
        )

        points[k] = run_time

    return points


def is_sorted(lst, key=lambda x: x):
    """
    Method that checks whether or not a list is sorted

    Args:
        lst: the list that will be checked
    Returns:
    bool:    True if the list is sorted, false otherwise.
    """
    return all(key(lst[i]) <= key(lst[i + 1]) for i in range(len(lst) - 1))
