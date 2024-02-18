from pydantic import BaseModel


class LoadNSIRequest(BaseModel):
    download_link: str
    data_type: int


class LoadNSIResponse(BaseModel):
    success: bool
    description: str


class GetNSIRequest(BaseModel):
    data_type: int


class GetNSIResponse(BaseModel):
    success: bool
    description: str
    data: list
