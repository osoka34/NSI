from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from internal.service.application_nsi import ApplicationNSIService
from internal.dto import LoadNSIRequest, GetNSIRequest

router = APIRouter()


@router.post('/load_nsi_data')
async def load_nsi_data(
    dto: LoadNSIRequest,
    application_service: ApplicationNSIService = Depends(),
) -> JSONResponse:
    """
    Load NSI data

    Args:
    dto (LoadNSIRequest): LoadNSIRequest

    Returns:
    JSONResponse: Default response with bool success and str message
    """
    return application_service.load_nsi_data(dto)


@router.post('/get_nsi_data')
async def get_nsi_data(
    dto: GetNSIRequest,
    application_service: ApplicationNSIService = Depends(),
) -> dict:
    """
    Get NSI data

    Args:
    dto (GetNSIRequest): GetNSIRequest

    Returns:
    dict: json response with nsi data
    """
    return application_service.get_nsi_data(dto)

