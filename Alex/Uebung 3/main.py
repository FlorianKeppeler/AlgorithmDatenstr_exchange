import matplotlib.pyplot as plt

from BucketSort import bucket_sort_performance
from RadixSort import radix_sort_performance


plt.style.use("ggplot")


# plot graph (lin and log)
def plot_performance(points_bucket: dict, points_radix: dict):
    x_pb, y_pb = zip(*points_bucket.items())
    x_pr, y_pr = zip(*points_radix.items())

    figure, axis = plt.subplots(2)

    axis[0].plot(x_pb, y_pb, label="bucket sort")
    axis[0].plot(x_pr, y_pr, label="radix sort")
    axis[0].legend()
    axis[0].set_title("Bucket sort and Radix sort, linear scale")
    axis[0].set_xlabel("List size")
    axis[0].set_ylabel("Time, sec")

    axis[1].plot(x_pb, y_pb, label="bucket sort")
    axis[1].plot(x_pr, y_pr, label="radix sort")
    axis[1].legend()
    axis[1].set_yscale("log")
    axis[1].set_title("Bucket sort and Radix sort, log scale")
    axis[1].set_xlabel("List size")
    axis[1].set_ylabel("Time, sec")

    plt.legend()
    plt.show()


def main():
    k_values_start = 2 * 10**4
    k_values_end = (12 * (10**5)) + 1
    k_values_step = 2 * 10**4
    array_size = 10**4

    pb = bucket_sort_performance(
        array_size, k_values_start, k_values_end, k_values_step
    )
    pr = radix_sort_performance(
        array_size, k_values_start, k_values_end, k_values_step
    )

    plot_performance(pb, pr)


if __name__ == "__main__":
    main()
