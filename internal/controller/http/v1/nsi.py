from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from internal.service.application import ApplicationService
from internal.dto import LoadNSIRequest, GetNSIRequest

router = APIRouter()


@router.post('/load_nsi_data')
async def load_nsi_data(
    dto: LoadNSIRequest,
    # application_service: ApplicationService = ApplicationService(),
    # dto: LoadNSIRequest = Depends(),
) -> JSONResponse:
    application_service: ApplicationService = ApplicationService()
    return application_service.load_nsi_data(dto)


@router.post('/get_nsi_data')
async def get_nsi_data(
    dto: GetNSIRequest,
    # dto: GetNSIRequest = Depends(),
) -> dict:
    application_service: ApplicationService = ApplicationService()
    return application_service.get_nsi_data(dto)

