from fastapi import APIRouter
from starlette.responses import JSONResponse

router = APIRouter()


@router.get('')
async def health() -> JSONResponse:
    """
    Health check

    Returns:
    JSONResponse: Health check status
    """
    return JSONResponse(
        content={"status": "OK"},
        status_code=200
    )