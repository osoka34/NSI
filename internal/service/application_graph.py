from internal.dto import GetShortPathRequest, GRAPH_BAD_REQUEST
from starlette.responses import JSONResponse
from internal.usecase.graph_algo import short_path
from internal.usecase.utils import to_matrix
from internal.usecase.graph_algo.ant_colony_all_points import ACO_TSP
from internal.usecase.graph_algo.ant_colony import calculate_path_and_cost
from internal.service import HTTP_200_OK, INTERNAL_ERROR
from internal.usecase.utils import validate_size


class ApplicationGraphService(object):
    def __init__(self):
        """
        Constructor for ApplicationGraphService class.
        """
        pass

    def ant_colony(self, req: GetShortPathRequest) -> JSONResponse:
        """
        Ant colony algorithm for finding the shortest path and cost in a graph.

        Args:
        req: GetShortPathRequest - request object

        Example:
            {
                "start_node": 0,
                "end_node": 9,
                "size": 10,
                "flatten_matrix": [0.74788737, 0.28540867, 0.99959624, 0.10110528, 0.3926201,  0.40042853, 0.635031, 0.56465142, 0.72817825, 0.19600194, 0.39843629, 0.87502986, 0.22554879, 0.18716884, 0.70307813, 0.4830509, 0.25361671, 0.6572518, 0.36114295, 0.440903]
            }

        Returns:
        JSONResponse - response object

        Examples:
            Success 200:
            {
                "shortest_path": [1, 2, 3, 4],
                "cost": 10.0,
                "success": true,
                "description": "ok"
            }
            Failure 400:
            {
                "success": false,
                "description": "Matrix size does not match the specified size"
            }
            Failure 500:
            {
                "success": false,
                "description": "Internal server error"
            }
        """
        try:
            if not validate_size(req):
                return GRAPH_BAD_REQUEST

            graph = to_matrix(req.flatten_matrix, req.size)

            path, cost = calculate_path_and_cost(graph, req.size, req.start_node, req.end_node)
            return JSONResponse(content={
                "shortest_path": path,
                "cost": cost,
                "success": True,
                "description": "ok"
            },
                status_code=HTTP_200_OK
            )
        except Exception as e:
            print(f"ERROR ::: ApplicationGraphService -> ant_colony: {e}")
            return INTERNAL_ERROR

    def dijkstra(self, req: GetShortPathRequest) -> JSONResponse:
        """
        Dijkstra algorithm for finding the shortest path and cost in a graph.

        Args:
        req: GetShortPathRequest - request object

        Example:
            {
                "start_node": 0,
                "end_node": 9,
                "size": 10,
                "flatten_matrix": [0.74788737, 0.28540867, 0.99959624, 0.10110528, 0.3926201,  0.40042853, 0.635031, 0.56465142, 0.72817825, 0.19600194, 0.39843629, 0.87502986, 0.22554879, 0.18716884, 0.70307813, 0.4830509, 0.25361671, 0.6572518, 0.36114295, 0.440903]
            }

        Returns:
        JSONResponse - response object

        Examples:
            Success 200:
            {
                "shortest_path": [1, 2, 3, 4],
                "cost": 10.0,
                "success": true,
                "description": "ok"
            }
            Failure 400:
            {
                "success": false,
                "description": "Matrix size does not match the specified size"
            }
            Failure 500:
            {
                "success": false,
                "description": "Internal server error"
            }
        """
        try:
            if not validate_size(req):
                return GRAPH_BAD_REQUEST

            graph = to_matrix(req.flatten_matrix, req.size)

            path, cost = short_path(graph, req.start_node, req.end_node)
            return JSONResponse(content={
                "shortest_path": path,
                "cost": cost,
                "success": True,
                "description": "ok"
            },
                status_code=HTTP_200_OK
            )
        except Exception as e:
            print(f"ERROR ::: ApplicationGraphService -> dijkstra: {e}")
            return INTERNAL_ERROR
