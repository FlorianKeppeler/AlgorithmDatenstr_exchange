import random
import math
import time

import matplotlib.pyplot as plt
from pprint import pprint

plt.style.use("ggplot")


def merge_sort(nums: list[int], k: int):
    if not nums:
        raise ValueError("Given list is empty!")

    n = len(nums)

    if k > n:
        raise ValueError(f"Can't divide list with {n} elemets into {k} parts!")

    tmp = [0] * n

    # we will need x // y and x % y values
    # to correctly divide given list into
    # k blocks
    p1, p2 = divmod(n, k)

    sub_lists_indexes = []
    for i in range(k):
        # divide into approx. equal parts
        # it's not always possible to have exactly equal parts,
        # for example when we have 12 elements and k = 5,
        # or in general, when n % k != 0

        block_start = i * p1 + min(i, p2)
        block_end = (i + 1) * p1 + min(i + 1, p2)

        # Save indexes for merge operation
        # (instead of creating new arrays directly
        # we will subdivide the existing one into k approx. equal parts)
        sub_lists_indexes.append((block_start, block_end))

        # Perform merge sort on k parts
        merge_sort_recursive(nums, block_start, block_end, tmp)

    # Create "pointers" for sorted block to sort among them
    ptrs = [0] * k

    rslt = []

    # merge

    # If any element is left in it's corresponding block then
    # we will get True and the while loop will continue
    # We will finish when all "pointers" will reach the end
    # of correspondig blocks
    while any(
        ptrs[j] < (blocks[1] - blocks[0]) for j, blocks in enumerate(sub_lists_indexes)
    ):
        min_value = float("inf")
        min_idx = -1

        for i in range(k):
            # Go through every sorted block
            current_block_start, current_block_end = sub_lists_indexes[i]
            block = nums[current_block_start:current_block_end]

            # Pick the current min value across block and change min index
            if ptrs[i] < len(block) and block[ptrs[i]] < min_value:
                min_value = block[ptrs[i]]
                min_idx = i

        rslt.append(min_value)
        ptrs[min_idx] += 1

    return rslt


# Implementation of a recursive merge sort from lecture notes
def merge_sort_recursive(nums: list[int], start: int, end: int, tmp: list[int]):
    if end - start > 1:
        middle = (start + end) // 2
        merge_sort_recursive(nums, start, middle, tmp)
        merge_sort_recursive(nums, middle, end, tmp)

        pos = start
        i = start
        j = middle

        while pos < end:
            if i < middle and (j >= end or nums[i] <= nums[j]):
                tmp[pos] = nums[i]
                pos += 1
                i += 1

            else:
                tmp[pos] = nums[j]
                pos += 1
                j += 1

        for i in range(start, end):
            nums[i] = tmp[i]

        return nums


def measure_merge_sort(
    iterations: int, start: int, step: int, measure_points: list
) -> dict[int, list[float]]:
    time_dict = dict()

    for measure_point in measure_points:
        time_deltas = dict()
        for list_length in range(start, iterations + step, step):
            random_list = [random.randint(-10_000, 10_000) for _ in range(list_length)]

            match measure_point:
                case int():
                    time_start = time.time()
                    merge_sort(random_list, measure_point)
                    delta = time.time() - time_start
                    time_deltas[list_length] = delta
                case _:
                    time_start = time.time()
                    _, func = measure_point[0], measure_point[1]
                    merge_sort(random_list, func(list_length))
                    delta = time.time() - time_start
                    time_deltas[list_length] = delta

            print(
                f"List length: {list_length}\nMeasure point: {measure_point}\nTime: {delta}\n"
            )

        if isinstance(measure_point, tuple):
            time_dict[measure_point[0]] = time_deltas
        else:
            time_dict[measure_point] = time_deltas
    return time_dict


def plot_measurements(measurements: dict) -> None:
    for k, coords in measurements.items():
        sorted_by_list_legth = sorted(coords.items())  # sort by key (key = list length)
        x, y = zip(*sorted_by_list_legth)

        plt.plot(x, y, label=k)

    plt.xlabel("List size")
    plt.ylabel("Time, sec")
    plt.title("Merge sort performance measurement for different partitions")
    plt.legend()
    plt.show()


def main():
    iterations = 10000
    step = 50
    start = 50
    ks = [
        2,
        3,
        ("log_2(n)", lambda n: math.ceil(math.log2(n))),
        ("ceil(n / 4)", lambda n: math.ceil(n / 4)),
    ]

    measurements = measure_merge_sort(iterations, start, step, ks)

    plot_measurements(measurements)

    # n = 1000
    # k_limit = 20
    # for k in range(2, k_limit):
    #     arr = [random.randint(0, 10000) for _ in range(n)]
    #     sorted_arr = merge_sort(arr, k)

    #     if not sorted_arr == sorted(arr):
    #         raise Exception("Didn't Sort Correctly!")

    # print("seems to work")


if __name__ == "__main__":
    main()
