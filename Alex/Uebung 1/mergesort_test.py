import unittest
import random

from mergeSort import merge_sort


class MergeSortTest(unittest.TestCase):

    # Test K - merge sort
    def test_merge_sort(self):
        n = 1000
        k_limit = 20
        for k in range(2, k_limit):
            arr = [random.randint(0, 10000) for _ in range(n)]
            sorted_arr = merge_sort(arr, k)

            self.assertEqual(sorted_arr, sorted(arr))


if __name__ == "__main__":
    unittest.main()
