from pydantic import BaseModel

from starlette.responses import JSONResponse


class GetShortPathRequest(BaseModel):
    """
    Request model for get_short_path in graph

    Attributes:
    start_node: int - start node in the graph
    end_node: int - end node in the graph
    size: int - size of input array
    flatten_matrix: list - coordinates of the nodes in the graph
    """
    start_node: int
    end_node: int
    size: int
    flatten_matrix: list


GRAPH_BAD_REQUEST = JSONResponse(
    content={
        "success": False,
        "description": "Matrix size does not match the specified size"
    },
    status_code=400
)
