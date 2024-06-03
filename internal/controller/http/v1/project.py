from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from internal.service import ApplicationProjectService
from internal.dto import ProjectDto

router = APIRouter()


@router.get('/get/{in_id}')
async def get_one_project(
    in_id: int,
    application_service: ApplicationProjectService = Depends(),
) -> JSONResponse:
    return application_service.get_project_by_id(in_id)


@router.get('/get_all')
async def get_all_project(
    application_service: ApplicationProjectService = Depends(),
) -> JSONResponse:
    return application_service.get_all_project()


@router.post('/add')
async def add_project(
    dto: ProjectDto,
    application_service: ApplicationProjectService = Depends(),
) -> JSONResponse:
    return application_service.add_project(dto)


@router.delete('/delete/{in_id}')
async def delete_project(
    in_id: int,
    application_service: ApplicationProjectService = Depends(),
) -> JSONResponse:
    return application_service.delete_project(in_id)


@router.post('/update')
async def update_project(
    dto: ProjectDto,
    application_service: ApplicationProjectService = Depends(),
) -> JSONResponse:
    return application_service.update_project(dto)
