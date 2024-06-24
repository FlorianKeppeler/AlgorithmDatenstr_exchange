"""
Approximating TSP using fast MST-Algorithms

Copyright 2020, University of Freiburg

Philipp Schneider <philipp.schneider@cs.uni-freiburg.de>
"""

import heapq  # noqa
import math  # noqa
import random

from AdjacencyMatrix import AdjacencyMatrix  # noqa

# from networkx.utils.union_find import UnionFind # noqa
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


# Custom class for visualising TSP solution.
class TSPPlotter:

    def __init__(self):
        self.fig = plt.figure(tight_layout=True)
        self.gs = gridspec.GridSpec(3, 3)

    def visualize_routes(self, paths, points, num_iters=1):
        # plt.subplot(3, 1, 1)

        """
        path: List of lists with the different orders in which the nodes are visited
        points: coordinates for the different nodes
        num_iters: number of paths that are in the path list
        """

        # Unpack the primary TSP path and transform it into a list of ordered
        # coordinates
        ax = self.fig.add_subplot(self.gs[:, :2])

        x = []
        y = []
        for i in paths[0]:
            x.append(points[i][0])
            y.append(points[i][1])

        ax.plot(x, y, "co")

        # Set a scale for the arrow heads
        a_scale = float(max(x)) / float(100)

        # Draw the older paths, if provided
        if num_iters > 1:

            for i in range(1, num_iters):

                # Transform the old paths into a list of coordinates
                xi = []
                yi = []
                for j in paths[i]:
                    xi.append(points[j][0])
                    yi.append(points[j][1])

                ax.arrow(
                    xi[-1],
                    yi[-1],
                    (xi[0] - xi[-1]),
                    (yi[0] - yi[-1]),
                    head_width=a_scale,
                    color="r",
                    length_includes_head=True,
                    ls="dashed",
                    width=0.001 / float(num_iters),
                )
                for i in range(0, len(x) - 1):
                    plt.arrow(
                        xi[i],
                        yi[i],
                        (xi[i + 1] - xi[i]),
                        (yi[i + 1] - yi[i]),
                        head_width=a_scale,
                        color="r",
                        length_includes_head=True,
                        ls="dashed",
                        width=0.001 / float(num_iters),
                    )

        # Draw the primary path for the TSP problem
        ax.arrow(
            x[-1],
            y[-1],
            (x[0] - x[-1]),
            (y[0] - y[-1]),
            head_width=a_scale,
            color="g",
            length_includes_head=True,
        )
        for i in range(0, len(x) - 1):
            ax.arrow(
                x[i],
                y[i],
                (x[i + 1] - x[i]),
                (y[i + 1] - y[i]),
                head_width=a_scale,
                color="g",
                length_includes_head=True,
            )
            plt.pause(0.5)

        # Set axis too slitghtly larger than the set of x and y
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.relim()


def euclidian_dist(coord_0, coord_1):
    return math.sqrt((coord_0[0] - coord_1[0]) ** 2 + (coord_0[1] - coord_1[1]) ** 2)
            

def compute_tour(am: AdjacencyMatrix):
    """
    computes a tour which as an array tour[0],...,tour[n-1]
    containing the nodes {0,...,n-1}) of a graph given as
    Adjacency matrix that has a small sum of edge weights of
    a roundtrip defined as:
    w(tour[0],tour[1]) + ...
                       + w(tour[n-2],tour[n-1])
                       + w(tour[n-1],tour[0])
    the guarantee is that the weight of the computed tour
    is at most twice that of the best possible tour.

    Parameter:
        am - Instance of AdjacencyMatrix

    Returns:
        an array of size n representing the order in which
        nodes are visited (in a roundtrip)
    """
    nodes = [i for i in range(am.n)]

    current_node = random.choice(nodes)
    tour = [current_node]

    # Not sure
    # a bit faster remove and potential avoidence of duplicates
    free_nodes = set(nodes)
    # Remove already visited
    free_nodes.remove(current_node)

    while free_nodes:
        next_node = min(
            free_nodes,
            key=lambda x: euclidian_dist(am.matrix[current_node], am.matrix[x]),
        )  # Nearest neighbour
        free_nodes.remove(next_node)
        tour.append(next_node)
        current_node = next_node

    return tour

    # H = []
    # heapq.heapify(H)
    # distance = lambda x1, x2: math.sqrt(x1**2 + x2**2)

    # # Start innter loop from 1, to avoid 0 (for all v in V \ {s})
    # for i in range(1, am.n):
    #     # python heapq allows to generalize heaps
    #     # with simple element into heaps with tuples
    #     # but the first element should be
    #     # the "metric"
    #     # Hence we will need to define u a bit different
    #     # u := (d_u, marked:bool, index (u in lecture notes))
    #     heapq.heappush(H, (float("inf"), False, i))

    # # (s, 0)
    # heapq.heappush(H, (0, 0))

    # while H:
    #     u = heapq.heappop(H)
    #     # because we are storing graph in adjecency matrix
    #     # we can acsess each neighbour with (u[2], j),
    #     # where u[2] is the index of the current vertex (see line 53)

    #     for j in range(am.n):
    #         pass
    #         ##if am.get_weight(u[2], j) < distance():


def tour_weight(am, tour):
    """
    computes the sum of edge weigths when all nodes of a
    tour are visited as a roundtrip

    Parameter:
        am - Instance of AdjacencyMatrix of size n
        tour - permuation of {0,...,n-1}

    Returns:
        the following value rounded to two decimal places
        w(tour[0],tour[1]) + ...
                       + w(tour[n-1],tour[n-1])
                       + w(tour[n-1],tour[0])
    """
    n = am.node_size()
    weight_sum = 0
    for i in range(n - 1):
        weight_sum += am.get_weight(tour[i], tour[i + 1])
    weight_sum += am.get_weight(tour[n - 1], tour[0])
    return round(weight_sum, 2)


def read_graph_from_file(filename):
    """
    reads a complete weighted graph from a file (that must
    be loated in same folder) and creates an adjacency matrix
    from it

    Parameter:
        filename - name of file

    Returns:
        instance of AdjacencyMatrix representing the file
    """
    with open(filename) as input:
        lines = input.read().splitlines()
        # first line contains the number of nodes
        am = AdjacencyMatrix(int(lines[0]))

        # other lines contain edges seperated by a whitespace
        for i in range(0, len(lines) - 1):
            for j in range(am.node_size()):
                entries = lines[i + 1].split(" ")
                am.set_weight(i, j, float(entries[j]))

    return am
