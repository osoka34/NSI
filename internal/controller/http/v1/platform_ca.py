from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from internal.service import ApplicationPlatformCAService
from internal.dto import PlatformCADto

router = APIRouter()


@router.get('/get/{in_id}')
async def get_one_platform_ca(
    in_id: int,
    application_service: ApplicationPlatformCAService = Depends(),
) -> JSONResponse:
    return application_service.get_platform_ca_by_id(in_id)


@router.get('/get_all')
async def get_all_platform_ca(
    application_service: ApplicationPlatformCAService = Depends(),
) -> JSONResponse:
    return application_service.get_all_platform_ca()


@router.post('/add')
async def add_platform_ca(
    dto: PlatformCADto,
    application_service: ApplicationPlatformCAService = Depends(),
) -> JSONResponse:
    return application_service.add_platform_ca(dto)


@router.post('/update')
async def update_platform_ca(
    dto: PlatformCADto,
    application_service: ApplicationPlatformCAService = Depends(),
) -> JSONResponse:
    return application_service.update_platform_ca(dto)


@router.delete('/delete/{in_id}')
async def delete_platform_ca(
    in_id: int,
    application_service: ApplicationPlatformCAService = Depends(),
) -> JSONResponse:
    return application_service.delete_platform_ca(in_id)