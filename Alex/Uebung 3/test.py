import unittest
import random

from BucketSort import bucket_sort
from RadixSort import radix_sort


class BucketSortTest(unittest.TestCase):

    # Test Bucket sort
    def test_bucket_sort(self):

        for _ in range(100):
            k = random.randint(1_500, 2_000)
            array = [random.randint(0, 1000) for _ in range(100)]
            bucket_sort(array, k)
            self.assertEqual(array, sorted(array))

    def test_k_values(self):
        for _ in range(100):
            array = [random.randint(0, 1000) for _ in range(100)]
            k = random.randint(-1_150, 1_500)

            if k < 0:
                # funny syntax with assert raises
                self.assertRaises(ValueError, bucket_sort, array, k)

    def test_empty_lists(self):
        self.assertEqual(bucket_sort([], 10), None)
        self.assertEqual(bucket_sort([], 1), None)
        self.assertEqual(bucket_sort([], 3), None)


class RatixSortTest(unittest.TestCase):

    # Test Bucket sort
    def test_radix_sort(self):
        for _ in range(100):
            k = random.randint(1_500, 2_000)
            array = [random.randint(0, 1000) for _ in range(100)]
            radix_sort(array, k)
            self.assertEqual(array, sorted(array))

    def test_k_values(self):
        for _ in range(100):
            array = [random.randint(0, 1000) for _ in range(100)]
            k = random.randint(-1_500, 1_500)

            if k < 0:
                # funny syntax with assert raises
                self.assertRaises(ValueError, radix_sort, array, k)

    def test_empty_lists(self):
        self.assertEqual(bucket_sort([], 50), None)
        self.assertEqual(bucket_sort([], 2), None)
        self.assertEqual(bucket_sort([], 1), None)


if __name__ == "__main__":
    unittest.main()
