from pydantic import BaseModel


class CloudlinesDto(BaseModel):
    id: int
    synoptic_index_of_the_station: int
    year: int
    type_of_cloudiness: int
    average_cloudiness_in_january: str
    average_cloudiness_in_february: str
    average_cloudiness_in_march: str
    average_cloudiness_in_april: str
    average_cloudiness_in_may: str
    average_cloudiness_in_june: str
    average_cloudiness_in_july: str
    average_cloudiness_in_august: str
    average_cloudiness_in_september: str
    average_cloudiness_in_october: str
    average_cloudiness_in_november: str
    average_cloudiness_in_december: str

