from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from internal.service import ApplicationGroundPointsService
from internal.dto import GroundPointsDto

router = APIRouter()


@router.get('/get/{in_id}')
async def get_one_ground_points(
    in_id: int,
    application_service: ApplicationGroundPointsService = Depends(),
) -> JSONResponse:
    return application_service.get_ground_points_by_id(in_id)


@router.get('/get_all')
async def get_all_ground_points(
    application_service: ApplicationGroundPointsService = Depends(),
) -> JSONResponse:
    return application_service.get_all_ground_points()


@router.post('/add')
async def add_ground_points(
    dto: GroundPointsDto,
    application_service: ApplicationGroundPointsService = Depends(),
) -> JSONResponse:
    return application_service.add_ground_points(dto)


@router.post('/update')
async def update_ground_points(
    dto: GroundPointsDto,
    application_service: ApplicationGroundPointsService = Depends(),
) -> JSONResponse:
    return application_service.update_ground_points(dto)


@router.delete('/delete/{in_id}')
async def delete_ground_points(
    in_id: int,
    application_service: ApplicationGroundPointsService = Depends(),
) -> JSONResponse:
    return application_service.delete_ground_points(in_id)

