import random


def merge_sort(nums: list[int], k: int):
    
    if not nums:
        raise ValueError("Given list is empty!")
       
    n = len(nums)
    
    if k > n:
        raise ValueError(f"Can't divide list with {n} elemets into {k} parts!")
    
    tmp = [0] * n

    # we will need x // y and x % y values
    # to correctly divide given list into
    # k pieces
    p1, p2 = divmod(n, k)

    sub_lists_indexes = []
    for i in range(k):
        # subdivide into approx. equal parts 
        # it's not always possible, 
        # for example when we have 12 elements and k = 5)
        block_start = i * p1 + min(i, p2)
        block_end = (i+1) * p1 + min(i + 1, p2)
        
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
    #
    while any(ptrs[j] < (blocks[1] - blocks[0]) for j, blocks in enumerate(sub_lists_indexes)):
     
        min_value = float("inf")
        min_idx = -1

        for i in range(k):
            # Go through every sorted block
            current_block_start, current_block_end = sub_lists_indexes[i]
            block = nums[current_block_start : current_block_end]

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

def main():

    n = 1000
    k_limit = 20
    for k in range(2, k_limit):
        arr = [random.randint(0, 10000) for _ in range(n)]
        sorted_arr = merge_sort(arr, k)

        if not sorted_arr == sorted(arr):
            raise Exception("Didn't Sort Correctly!")
        
    print("seems to work")


if __name__ == "__main__":
    main()
