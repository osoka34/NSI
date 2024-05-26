from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from internal.service import ApplicationCloudStationService
from internal.dto import CloudStationDto

router = APIRouter()


@router.get('/get/{in_id}')
async def get_one_cloud_station(
    in_id: int,
    application_service: ApplicationCloudStationService = Depends(),
) -> JSONResponse:
    return application_service.get_cloud_station_by_id(in_id)


@router.get('/get_all')
async def get_all_cloud_station(
    application_service: ApplicationCloudStationService = Depends(),
) -> JSONResponse:
    return application_service.get_all_cloud_station()


@router.post('/add')
async def add_cloud_station(
    dto: CloudStationDto,
    application_service: ApplicationCloudStationService = Depends(),
) -> JSONResponse:
    return application_service.add_cloud_station(dto)


@router.post('/update')
async def update_cloud_station(
    dto: CloudStationDto,
    application_service: ApplicationCloudStationService = Depends(),
) -> JSONResponse:
    return application_service.update_cloud_station(dto)


@router.delete('/delete/{in_id}')
async def delete_cloud_station(
    in_id: int,
    application_service: ApplicationCloudStationService = Depends(),
) -> JSONResponse:
    return application_service.delete_cloud_station(in_id)

