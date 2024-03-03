import numpy as np
from scipy.sparse.csgraph import dijkstra


def short_path(graph: np.ndarray, start_vertex: int) -> list:
    """
    Func for finding the shortest path from the start vertex to all other vertices

    Args:
    graph: np.ndarray - adjacency matrix
    start_vertex: int - start vertex
    return_predecessors: bool - return predecessors

    Returns:
    distances: np.ndarray - shortest distances
    """
    distances = dijkstra(graph, indices=start_vertex, return_predecessors=False)
    return list(distances)



# points_coordinate = [0.74788737, 0.28540867, 0.99959624, 0.10110528, 0.3926201,  0.40042853, 0.635031, 0.56465142, 0.72817825, 0.19600194, 0.39843629, 0.87502986, 0.22554879, 0.18716884, 0.70307813, 0.4830509, 0.25361671, 0.6572518, 0.36114295, 0.440903]
# points_coordinate = np.array(points_coordinate).reshape(10, 2)
# print(points_coordinate)
# distance_matrix = spatial.distance.cdist(points_coordinate, points_coordinate, metric='euclidean')
#
# res = short_path(distance_matrix, 0)
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

