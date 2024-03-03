from pydantic import BaseModel
from starlette.responses import JSONResponse


class LoadNSIRequest(BaseModel):
    """
    Request model for load_nsi method
    """
    download_link: str
    data_type: int


class DefaultResponse(BaseModel):
    """
    Default response model
    """
    success: bool
    description: str


class GetNSIRequest(BaseModel):
    """
    Request model for get_nsi method
    """
    data_type: int
    limit: int


class GetNSIResponse(BaseModel):
    """
    Response model for get_nsi method
    """
    success: bool
    description: str
    data: list


NSI_BAD_REQUEST = JSONResponse(
                content=DefaultResponse(
                    success=False,
                    description="Invalid data type"
                ).dict(),
                status_code=400,
            )
