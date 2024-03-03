from internal.dto import GetShortPathRequest, GRAPH_BAD_REQUEST
from starlette.responses import JSONResponse
from internal.usecase.graph_algo import short_path
from internal.usecase.utils import to_matrix
from internal.usecase.graph_algo.ant_colony import ACO_TSP
from internal.service import HTTP_200_OK, INTERNAL_ERROR
from internal.usecase.utils import validate_size



class ApplicationGraphService(object):
    def __init__(self):
        pass

    def ant_colony(self, req: GetShortPathRequest) -> JSONResponse:
        """
        Ant colony algorithm for finding the shortest path in a graph.

        Args:
        req: GetShortPathRequest - request object

        Returns:
        JSONResponse - response object

        """
        try:
            if not validate_size(req):
                return GRAPH_BAD_REQUEST

            graph = to_matrix(req.flatten_matrix, req.size)

            aca = ACO_TSP(
                n_dim=req.size,
                size_pop=40,  # количество муравьёв
                max_iter=10,
                distance_matrix=graph
            )
            res = aca.get_node_shortest_path(req.special_vertex)
            return JSONResponse(content={
                "shortest_path": res,
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
        Dijkstra algorithm for finding the shortest path in a graph.

        Args:
        req: GetShortPathRequest - request object

        Returns:
        JSONResponse - response object
        """
        try:
            if not validate_size(req):
                return GRAPH_BAD_REQUEST

            graph = to_matrix(req.flatten_matrix, req.size)

            res = short_path(graph, req.special_vertex)
            return JSONResponse(content={
                "shortest_path": res,
                "success": True,
                "description": "ok"
            },
                status_code=HTTP_200_OK
            )
        except Exception as e:
            print(f"ERROR ::: ApplicationGraphService -> dijkstra: {e}")
            return INTERNAL_ERROR