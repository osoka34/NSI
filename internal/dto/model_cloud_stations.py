from pydantic import BaseModel


class CloudStationDto(BaseModel):
    id: int
    index_vmo: int
    station_name: str
    latitude: str
    longitude: str
    height_homeopost: int
    collect_from: int
    note: str
