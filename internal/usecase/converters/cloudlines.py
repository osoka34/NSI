from internal.entity.cloudlines_repository import Cloudlines
from internal.dto import CloudlinesDto


def cloudlines_from_repo_to_dto(cloudlines: Cloudlines) -> CloudlinesDto:
    return CloudlinesDto(
        id=cloudlines.id,
        Synoptic_index_of_thу_station=cloudlines.Synoptic_index_of_thу_station,
        Year=cloudlines.Year,
        Type_of_cloudiness=cloudlines.Type_of_cloudiness,
        Average_cloudiness_in_January=cloudlines.Average_cloudiness_in_January,
        Average_cloudiness_in_February=cloudlines.Average_cloudiness_in_February,
        Average_cloudiness_in_March=cloudlines.Average_cloudiness_in_March,
        Average_cloudiness_in_April=cloudlines.Average_cloudiness_in_April,
        Average_cloudiness_in_May=cloudlines.Average_cloudiness_in_May,
        Average_cloudiness_in_June=cloudlines.Average_cloudiness_in_June,
        Average_cloudiness_in_July=cloudlines.Average_cloudiness_in_July,
        Average_cloudiness_in_August=cloudlines.Average_cloudiness_in_August,
        Average_cloudiness_in_September=cloudlines.Average_cloudiness_in_September,
        Average_cloudiness_in_October=cloudlines.Average_cloudiness_in_October,
        Average_cloudiness_in_November=cloudlines.Average_cloudiness_in_November,
        Average_cloudiness_in_December=cloudlines.Average_cloudiness_in_December
    )


def cloudlines_from_repo_to_dto_list(params: list[Cloudlines]) -> list[CloudlinesDto]:
    l = []
    for c in params:
        l.append(CloudlinesDto(
            id=c.id,
            Synoptic_index_of_thу_station=c.Synoptic_index_of_thу_station,
            Year=c.Year,
            Type_of_cloudiness=c.Type_of_cloudiness,
            Average_cloudiness_in_January=c.Average_cloudiness_in_January,
            Average_cloudiness_in_February=c.Average_cloudiness_in_February,
            Average_cloudiness_in_March=c.Average_cloudiness_in_March,
            Average_cloudiness_in_April=c.Average_cloudiness_in_April,
            Average_cloudiness_in_May=c.Average_cloudiness_in_May,
            Average_cloudiness_in_June=c.Average_cloudiness_in_June,
            Average_cloudiness_in_July=c.Average_cloudiness_in_July,
            Average_cloudiness_in_August=c.Average_cloudiness_in_August,
            Average_cloudiness_in_September=c.Average_cloudiness_in_September,
            Average_cloudiness_in_October=c.Average_cloudiness_in_October,
            Average_cloudiness_in_November=c.Average_cloudiness_in_November,
            Average_cloudiness_in_December=c.Average_cloudiness_in_December
        ))
    return l


def cloudlines_from_dto_to_repo(cloudlines: CloudlinesDto) -> Cloudlines:
    return Cloudlines(
        id=cloudlines.id,
        Synoptic_index_of_thу_station=cloudlines.Synoptic_index_of_thу_station,
        Year=cloudlines.Year,
        Type_of_cloudiness=cloudlines.Type_of_cloudiness,
        Average_cloudiness_in_January=cloudlines.Average_cloudiness_in_January,
        Average_cloudiness_in_February=cloudlines.Average_cloudiness_in_February,
        Average_cloudiness_in_March=cloudlines.Average_cloudiness_in_March,
        Average_cloudiness_in_April=cloudlines.Average_cloudiness_in_April,
        Average_cloudiness_in_May=cloudlines.Average_cloudiness_in_May,
        Average_cloudiness_in_June=cloudlines.Average_cloudiness_in_June,
        Average_cloudiness_in_July=cloudlines.Average_cloudiness_in_July,
        Average_cloudiness_in_August=cloudlines.Average_cloudiness_in_August,
        Average_cloudiness_in_September=cloudlines.Average_cloudiness_in_September,
        Average_cloudiness_in_October=cloudlines.Average_cloudiness_in_October,
        Average_cloudiness_in_November=cloudlines.Average_cloudiness_in_November,
        Average_cloudiness_in_December=cloudlines.Average_cloudiness_in_December
    )
