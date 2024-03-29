import numpy as np
from scipy.sparse.csgraph import dijkstra
from scipy import spatial


def short_path(graph: np.ndarray, start_node: int, end_node) -> tuple:
    """
    Func for finding the shortest path and cost using Dijkstra algorithm

    Args:
    graph: np.ndarray - adjacency matrix
    start_node: int - start node
    end_node: int - end node

    return_predecessors: bool - return predecessors

    Returns:
    path: list - list of the shortest path
    cost: float - the cost of the shortest path
    """
    distances, predecessors = dijkstra(graph, return_predecessors=True, indices=start_node)
    path = []
    while end_node != start_node:
        path.insert(0, end_node)
        end_node = predecessors[end_node]
    path.insert(0, start_node)

    cost = distances[end_node - 1,]
    return path, cost





# points_coordinate = [0.74788737, 0.28540867, 0.99959624, 0.10110528, 0.3926201,  0.40042853, 0.635031, 0.56465142, 0.72817825, 0.19600194, 0.39843629, 0.87502986, 0.22554879, 0.18716884, 0.70307813, 0.4830509, 0.25361671, 0.6572518, 0.36114295, 0.440903]
# points_coordinate = np.array(points_coordinate).reshape(10, 2)
# distance_matrix = spatial.distance.cdist(points_coordinate, points_coordinate, metric='euclidean')

# res = short_path(distance_matrix, 0, 9)
# print(res)


# graph_ex = [0, 2, 0, 1, 0, 2, 0, 4, 0, 0, 0, 4, 0, 3, 0, 1, 0, 3, 0, 5, 0, 0, 0, 5, 0]
# graph_ex = np.array(graph_ex).reshape(5, 5)
#
# # graph_ex = np.array([[0, 2, 0, 1, 0],
# #                   [2, 0, 4, 0, 0],
# #                   [0, 4, 0, 3, 0],
# #                   [1, 0, 3, 0, 5],
# #                   [0, 0, 0, 5, 0]])
#
#
# res = short_path(graph_ex, 0)
# print(res)

