from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from internal.service import ApplicationGraphService
from internal.dto import GetShortPathRequest

router = APIRouter()


@router.post('/ant_colony')
async def path_ant_colony(
    dto: GetShortPathRequest,
    application_service: ApplicationGraphService = Depends(),
) -> JSONResponse:
    """
    Get shortest path using ant colony algorithm

    Args:
    dto (GetShortPathRequest): GetShortPathRequest

    Returns:
    JSONResponse: json response with shortest path
    """
    return application_service.ant_colony(dto)


@router.post('/dijkstra')
async def path_dijkstra(
    dto: GetShortPathRequest,
    application_service: ApplicationGraphService = Depends(),
) -> JSONResponse:
    """
    Get shortest path using dijkstra algorithm

    Args:
    dto (GetShortPathRequest): GetShortPathRequest

    Returns:
    JSONResponse: json response with shortest path
    """
    return application_service.dijkstra(dto)