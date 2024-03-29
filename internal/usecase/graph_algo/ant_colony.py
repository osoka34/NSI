from aco_routing import ACO
import numpy as np
from scipy import spatial
import networkx as nx


def calculate_path_and_cost(graph: np.ndarray, size: int, start_node: int, end_node: int) -> tuple:
    """
    Func for calculating the shortest path and cost using ACO algorithm

    Args:
    points_coordinate: list - list of coordinates
    size: int - size of the list
    start_node: int - start node
    end_node: int - end node

    Returns:
    aco_path: list - list of the shortest path
    aco_cost: float - the cost of the shortest path
    """
    # points_coordinate = np.array(points_coordinate).reshape(size, 2)
    # distance_matrix = spatial.distance.cdist(points_coordinate, points_coordinate, metric='euclidean')

    G = nx.DiGraph()

    for i in range(size):
        for j in range(size):
            if i != j:
                G.add_edge(i, j, cost=graph[i][j])

    aco = ACO(G, ant_max_steps=100, num_iterations=100, ant_random_spawn=True)

    aco_path, aco_cost = aco.find_shortest_path(
        source=start_node,
        destination=end_node,
        num_ants=1000,
    )

    return aco_path, aco_cost

# points_coordinate = [0.74788737, 0.28540867,
#                      0.99959624, 0.10110528,
#                      0.3926201,  0.40042853,
#                      0.635031, 0.56465142,
#                      0.72817825, 0.19600194,
#                      0.39843629, 0.87502986,
#                      0.22554879, 0.18716884,
#                      0.70307813, 0.4830509,
#                      0.25361671, 0.6572518,
#                      0.36114295, 0.440903]


# points_coordinate = [0.74788737, 0.28540867, 0.99959624, 0.10110528, 0.3926201,  0.40042853, 0.635031, 0.56465142, 0.72817825, 0.19600194, 0.39843629, 0.87502986, 0.22554879, 0.18716884, 0.70307813, 0.4830509, 0.25361671, 0.6572518, 0.36114295, 0.440903]
# points_coordinate = np.array(points_coordinate).reshape(10, 2)
#
# graph = spatial.distance.cdist(points_coordinate, points_coordinate, metric='euclidean')
#
#
# #
# path, cost = calculate_path_and_cost(graph, 10, 0, 9)
# #
# print(f"ACO Path: {path}")
# print(f"ACO Cost: {cost}")
