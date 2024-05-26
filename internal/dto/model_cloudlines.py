from pydantic import BaseModel


class CloudlinesDto(BaseModel):
    id: int
    Synoptic_index_of_thу_station: int
    Year: int
    Type_of_cloudiness: int
    Average_cloudiness_in_January: str
    Average_cloudiness_in_February: str
    Average_cloudiness_in_March: str
    Average_cloudiness_in_April: str
    Average_cloudiness_in_May: str
    Average_cloudiness_in_June: str
    Average_cloudiness_in_July: str
    Average_cloudiness_in_August: str
    Average_cloudiness_in_September: str
    Average_cloudiness_in_October: str
    Average_cloudiness_in_November: str
    Average_cloudiness_in_December: str

