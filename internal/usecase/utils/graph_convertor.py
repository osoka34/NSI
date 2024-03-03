from scipy import spatial
import numpy as np


def to_matrix(flatten: list, size: int) -> np.ndarray:
    """
    Convert a list to a matrix

    Args:
    flatten: list - flatten list
    size: int - size of the matrix

    Returns:
    matrix: list - matrix
    """
    points_coordinate = np.array(flatten).reshape(size, 2)
    distance_matrix = spatial.distance.cdist(points_coordinate, points_coordinate, metric='euclidean')
    return distance_matrix



# points_coordinate = [0.74788737, 0.28540867, 0.99959624, 0.10110528, 0.3926201,  0.40042853, 0.635031, 0.56465142, 0.72817825, 0.19600194, 0.39843629, 0.87502986, 0.22554879, 0.18716884, 0.70307813, 0.4830509, 0.25361671, 0.6572518, 0.36114295, 0.440903]
# res = to_matrix(points_coordinate, 10)
# print(res)