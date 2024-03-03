from starlette.responses import JSONResponse

HTTP_200_OK = 200
HTTP_400_BAD_REQUEST = 400
HTTP_401_UNAUTHORIZED = 401
HTTP_403_FORBIDDEN = 403
HTTP_404_NOT_FOUND = 404
HTTP_500_INTERNAL_ERROR = 500


INTERNAL_ERROR = JSONResponse(
    content={"success": False, "description": "Internal error"},
    status_code=HTTP_500_INTERNAL_ERROR,
)