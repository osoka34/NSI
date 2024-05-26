from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from internal.service import ApplicationTelescopeSystemService
from internal.dto import TelescopeSystemDto

router = APIRouter()


@router.get('/get/{in_id}')
async def get_one_telescope_system(
    in_id: int,
    application_service: ApplicationTelescopeSystemService = Depends(),
) -> JSONResponse:
    return application_service.get_telescope_system_by_id(in_id)


@router.get('/get_all')
async def get_all_telescope_system(
    application_service: ApplicationTelescopeSystemService = Depends(),
) -> JSONResponse:
    return application_service.get_all_telescope_system()


@router.post('/add')
async def add_telescope_system(
    dto: TelescopeSystemDto,
    application_service: ApplicationTelescopeSystemService = Depends(),
) -> JSONResponse:
    return application_service.add_telescope_system(dto)


@router.post('/update')
async def update_telescope_system(
    dto: TelescopeSystemDto,
    application_service: ApplicationTelescopeSystemService = Depends(),
) -> JSONResponse:
    return application_service.update_telescope_system(dto)


@router.delete('/delete/{in_id}')
async def delete_telescope_system(
    in_id: int,
    application_service: ApplicationTelescopeSystemService = Depends(),
) -> JSONResponse:
    return application_service.delete_telescope_system(in_id)

