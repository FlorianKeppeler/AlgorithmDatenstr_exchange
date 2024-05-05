
from Queue import Queue 

from ListElement import ListElement

from BucketSort import bucket_sort

from math import log10, ceil

array = [14, 212, 34, 623, 52, 42]

# m = 2

# tmp = []

# for item in array:
#     tmp += [item % 10**1 // 10**0]

# print(array)
# bucket_sort(array, 10, lambda x: x % 10**1 // 10**0)
# print(array)
# bucket_sort(array, 10, lambda x: x % 10**2 // 10**1)
# print(array)
# bucket_sort(array, 10, lambda x: x % 10**3 // 10**2)
# print(array)


key = max(array)

m = ceil(log10(key))

print(m)

print(array)

for i in range(m):
    bucket_sort(array, 10, lambda x: x % 10**(i + 1) // 10**i)
    print(array)





# [print(queue_list[i]) for i in range(k + 1)]

# print(t.enqueue(ListElement(23)))
# print(t)
