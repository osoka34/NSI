from pydantic import BaseModel
from starlette.responses import JSONResponse


class LoadNSIRequest(BaseModel):
    """
    Request model for load_nsi method

    Attributes:
    download_link: str - link to the file
    data_type: int - type of the data

    Example:
    {
        "download_link": "https://www.example.com/data.txt",
        "data_type": 1
    }
    """
    download_link: str
    data_type: int


class DefaultResponse(BaseModel):
    """
    Default response model

    Attributes:
    success: bool
    description: str

    Example:
    {
        "success": true,
        "description": "Data loaded"
    }
    """
    success: bool
    description: str


class GetNSIRequest(BaseModel):
    """
    Request model for get_nsi method

    Attributes:
    data_type: int
    limit: int

    Example:
    {
        "data_type": 1,
        "limit": 10
    }
    """
    data_type: int
    limit: int


class GetNSIResponse(BaseModel):
    """
    Response model for get_nsi method

    Attributes:
    success: bool
    description: str
    data: list

    Example:
    {
        "success": true,
        "description": "Data loaded"
        "data": [
            {
                "id": 1,
                "value1": "val",
                "value2": 30
            },
            {
                "id": 2,
                "value1": "val",
                "age": 25
            }
        ]
    }
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
