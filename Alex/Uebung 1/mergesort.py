import random


def merge_sort(nums: list[int], k):
    
    if not nums:
        raise ValueError("Passed list is empty!")
    
    tmp = [0] * len(nums)
    merge_sort_recursive(nums, 0, len(nums), tmp)

    return nums


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
            

def main():
    n = 1000
    k_limit = 20
    for k in range(2, k_limit):
        arr = [random.randint(0, 10000) for i in range(n)]
        sorted_arr = merge_sort(arr, k)
        if not sorted_arr == sorted(arr):
            raise Exception("Didn't Sort Correctly!")
    print("seems to work")


if __name__ == "__main__":
    main()
