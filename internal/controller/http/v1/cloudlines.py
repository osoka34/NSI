from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from internal.service import ApplicationCloudlinesService
from internal.dto import CloudlinesDto

router = APIRouter()


@router.get('/get/{in_id}')
async def get_one_cloudlines(
    in_id: int,
    application_service: ApplicationCloudlinesService = Depends(),
) -> JSONResponse:
    return application_service.get_cloudlines_by_id(in_id)


@router.get('/get_all')
async def get_all_cloudlines(
    application_service: ApplicationCloudlinesService = Depends(),
) -> JSONResponse:
    return application_service.get_all_cloudlines()


@router.post('/add')
async def add_cloudlines(
    dto: CloudlinesDto,
    application_service: ApplicationCloudlinesService = Depends(),
) -> JSONResponse:
    return application_service.add_cloudlines(dto)


@router.post('/update')
async def update_cloudlines(
    dto: CloudlinesDto,
    application_service: ApplicationCloudlinesService = Depends(),
) -> JSONResponse:
    return application_service.update_cloudlines(dto)


@router.delete('/delete/{in_id}')
async def delete_cloudlines(
    in_id: int,
    application_service: ApplicationCloudlinesService = Depends(),
) -> JSONResponse:
    return application_service.delete_cloudlines(in_id)

