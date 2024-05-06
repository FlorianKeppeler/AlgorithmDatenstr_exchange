

import matplotlib.pyplot as plt

from BucketSort import bucket_sort_performance
from RadixSort import radix_sort_performance


plt.style.use("ggplot")

radix_res = radix_sort_performance()
bucket_res = bucket_sort_performance()
# print(list(radix_res.keys()))

plt.plot(list(bucket_res.keys()),
         list(bucket_res.values()), label="bucket sort")
plt.plot(list(radix_res.keys()),
         list(radix_res.values()), label="radix sort")

plt.title("Laufzeit BucketSort vs. RadixSort")
plt.ylabel("Laufzeit [s]")
plt.xlabel("Größe von k")
plt.legend()

plt.savefig("Laufzeit.png")
