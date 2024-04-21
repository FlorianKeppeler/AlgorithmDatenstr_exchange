from MergeSort import merge_sort
from typing import Callable
import math
from random import randint
from time import time

import matplotlib.pyplot as plt

plt.style.use("ggplot")


assert merge_sort([12, 11, 13, 5, 6, 7], 3) == [5, 6, 7, 11, 12, 13]


def get_time_int(n: list[int], k: int) -> list[int]:

    diff = []

    for i in n:

        arr = [randint(0, 10000) for i in range(i)]

        pre = time()
        merge_sort(arr, k)
        post = time()

        diff += [post - pre]

    return diff


def get_time_func(n: list[int], f: Callable[[list[int]], int]) -> list[int]:

    diff = []

    for i in n:

        arr = [randint(0, 10000) for i in range(i)]

        k = f(arr)

        pre = time()
        merge_sort(arr, k)
        post = time()

        diff += [post - pre]

    return diff


n = [x * 100 for x in range(1, 101)]

k = 2

res = get_time_int(n, k)
plt.plot(n, res, label=k)

k = 3

res = get_time_int(n, k)
plt.plot(n, res, label=k)

res = get_time_func(n, lambda x: int(math.log2(len(x))))
plt.plot(n, res, label="log2(n)")

res = get_time_func(n, lambda x: int(len(x) / 4))
plt.plot(n, res, label="n/4")


plt.xlabel("Länge der zu sortierenden Liste")
plt.ylabel("Laufzeit [sec]")
plt.title("Laufzeit merge_sort für unterschiedliche k")
plt.legend()
plt.savefig("Laufzeit.png")


# try:
#     merge_sort([12, 11, 13, 5, 6, 7], 10)
# except ValueError:
#     print("k > length array raises correct error")


# if __name__ == "__main__":

#     assert merge_sort([12, 11, 13, 5, 6, 7], 3) == [5, 6, 7, 11, 12, 13]

#     n = 1000
#     k_limit = 20
#     for k in range(2, k_limit):
#         arr = [random.randint(0, 10000) for i in range(n)]
#         sorted_arr = merge_sort(arr, k)
#         if not sorted_arr == sorted(arr):
#             raise Exception("Didn't Sort Correctly!")
#     print("seems to work")
