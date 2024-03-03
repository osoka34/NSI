from pydantic import BaseModel

from starlette.responses import JSONResponse

class GetShortPathRequest(BaseModel):
    """
    Request model for get_short_path in graph
    """
    special_vertex: int
    size: int
    flatten_matrix: list


GRAPH_BAD_REQUEST = JSONResponse(
    content={
        "success": False,
        "description": "Matrix size does not match the specified size"
    },
    status_code=400
)
