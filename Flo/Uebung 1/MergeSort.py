import random


def merge_sort(arr: list[int], k: int) -> list[int]:

    if len(arr) == 0:
        raise ValueError("list is empty")

    if len(arr) < k:
        raise ValueError("k must be >= than list")

    # divide arr in k equal parts
    start = 0
    end = len(arr)

    k_index = int(start + (end - start) / k)  # how many elements per part?

    tmp_arr = []
    tmp_end = 0

    # for each iteration elements get stored in k parts. Remaining elements will be stored in one additional partition
    while tmp_end < len(arr):

        tmp_end = start + k_index
        tmp_arr += [arr[start:tmp_end]]
        start = tmp_end

    # as long as elements of parts are > k merge_sort will be run recursively
    for x in tmp_arr:
        if len(x) > 1:
            if len(x) >= k:
                merge_sort(x, k)
            else:
                merge_sort(x, len(x) % k)  # if length of x is < than k, k will be adjusted in order to end up with only 1 element per part in the end of recursion


    # after division parts will be merged again while getting sorted
    for j in range(len(arr)):

        if len(tmp_arr) != 1:

            x = tmp_arr[0][0]

            i = 1
            tmp_i = 0

            while i < len(tmp_arr):

                if x > tmp_arr[i][0]:
                    x = tmp_arr[i][0]
                    tmp_i = i

                i += 1

            if len(tmp_arr[tmp_i]) == 1:
                del tmp_arr[tmp_i]
            else:
                del tmp_arr[tmp_i][0]

            arr[j] = x

        else:

            arr[j] = tmp_arr[0][0]

            if len(tmp_arr[0]) == 1:
                del tmp_arr[0]
            else:
                del tmp_arr[0][0]

    return arr


# testing some random arrays to help you check correctness
if __name__ == "__main__":

    assert merge_sort([12, 11, 13, 5, 6, 7], 3) == [5, 6, 7, 11, 12, 13]

    n = 1000
    k_limit = 20
    for k in range(2, k_limit):
        arr = [random.randint(0, 10000) for i in range(n)]
        sorted_arr = merge_sort(arr, k)
        if not sorted_arr == sorted(arr):
            raise Exception("Didn't Sort Correctly!")
    print("seems to work")
