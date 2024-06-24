import TSP as tsp


def main():

    route = tsp.read_graph_from_file("cities.txt")
    sol = tsp.compute_tour(route)
    wsum = tsp.tour_weight(route, sol)

    print("Cost: ", wsum)

    tsp_plotter = tsp.TSPPlotter()
    tsp_plotter.visualize_routes([sol], route.matrix)


if __name__ == "__main__":
    main()
