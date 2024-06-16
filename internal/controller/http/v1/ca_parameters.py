from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from internal.service import ApplicationCAParametersService
from internal.dto import CAParametersDto, CAPlatformViewDto

router = APIRouter()


@router.get('/get/{in_id}')
async def get_one_ca_parameters(
    in_id: int,
    application_service: ApplicationCAParametersService = Depends(),
) -> JSONResponse:
    return application_service.get_ca_parameters_by_id(in_id)


@router.get('/get_all')
async def get_all_ca_parameters(
    application_service: ApplicationCAParametersService = Depends(),
) -> JSONResponse:
    return application_service.get_all_ca_parameters()


@router.post('/add')
async def add_ca_parameters(
    dto: CAParametersDto,
    application_service: ApplicationCAParametersService = Depends(),
) -> JSONResponse:
    return application_service.add_ca_parameters(dto)


@router.post('/update')
async def update_ca_parameters(
    dto: CAParametersDto,
    application_service: ApplicationCAParametersService = Depends(),
) -> JSONResponse:
    return application_service.update_ca_parameters(dto)


@router.delete('/delete/{in_id}')
async def delete_ca_parameters(
    in_id: int,
    application_service: ApplicationCAParametersService = Depends(),
) -> JSONResponse:
    return application_service.delete_ca_parameters(in_id)


@router.get('/view/get_all')
async def get_one_ca_platform_view(
    application_service: ApplicationCAParametersService = Depends(),
) -> JSONResponse:
    return application_service.get_all_ca_platform_view()


@router.get('/view/get_all_by_id/{ca_id}')
async def get_all_ca_platform_view(
    ca_id: int,
    application_service: ApplicationCAParametersService = Depends(),
) -> JSONResponse:
    return application_service.get_all_by_id_ca_platform_view(ca_id)
