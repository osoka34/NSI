from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from internal.service import ApplicationNamedConstService
from internal.dto import NamedConstantsDto

router = APIRouter()


@router.get('/get/{in_id}')
async def get_one_named_const(
    in_id: int,
    application_service: ApplicationNamedConstService = Depends(),
) -> JSONResponse:
    return application_service.get_named_const_by_id(in_id)


@router.get('/get_all')
async def get_all_named_const(
    application_service: ApplicationNamedConstService = Depends(),
) -> JSONResponse:
    return application_service.get_all_named_const()


@router.post('/add')
async def add_named_const(
    dto: NamedConstantsDto,
    application_service: ApplicationNamedConstService = Depends(),
) -> JSONResponse:
    return application_service.add_named_const(dto)


@router.post('/update')
async def update_named_const(
    dto: NamedConstantsDto,
    application_service: ApplicationNamedConstService = Depends(),
) -> JSONResponse:
    return application_service.update_named_const(dto)


@router.delete('/delete/{in_id}')
async def delete_named_const(
    in_id: int,
    application_service: ApplicationNamedConstService = Depends(),
) -> JSONResponse:
    return application_service.delete_named_const(in_id)

