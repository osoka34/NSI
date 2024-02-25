from fastapi import APIRouter
from starlette.responses import JSONResponse

router = APIRouter()


@router.get('')
async def health() -> JSONResponse:
    return JSONResponse(
        content={"status": "OK"},
        status_code=200
    )