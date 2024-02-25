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
    """
    Load NSI data

    Args:
    dto (LoadNSIRequest): LoadNSIRequest

    Returns:
    JSONResponse: Default response with bool success and str message
    """
    application_service: ApplicationService = ApplicationService()
    return application_service.load_nsi_data(dto)


@router.post('/get_nsi_data')
async def get_nsi_data(
    dto: GetNSIRequest,
    # dto: GetNSIRequest = Depends(),
) -> dict:
    """
    Get NSI data

    Args:
    dto (GetNSIRequest): GetNSIRequest

    Returns:
    dict: json response with nsi data
    """
    application_service: ApplicationService = ApplicationService()
    return application_service.get_nsi_data(dto)

