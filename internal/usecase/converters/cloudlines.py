from internal.entity.cloudlines_repository import Cloudlines
from internal.dto import CloudlinesDto


def cloudlines_from_repo_to_dto(cloudlines: Cloudlines) -> CloudlinesDto:
    return CloudlinesDto(
        id=cloudlines.id,
        synoptic_index_of_the_station=cloudlines.synoptic_index_of_the_station,
        year=cloudlines.year,
        type_of_cloudiness=cloudlines.type_of_cloudiness,
        average_cloudiness_in_january=cloudlines.average_cloudiness_in_january,
        average_cloudiness_in_february=cloudlines.average_cloudiness_in_february,
        average_cloudiness_in_march=cloudlines.average_cloudiness_in_march,
        average_cloudiness_in_april=cloudlines.average_cloudiness_in_april,
        average_cloudiness_in_may=cloudlines.average_cloudiness_in_may,
        average_cloudiness_in_june=cloudlines.average_cloudiness_in_june,
        average_cloudiness_in_july=cloudlines.average_cloudiness_in_july,
        average_cloudiness_in_august=cloudlines.average_cloudiness_in_august,
        average_cloudiness_in_september=cloudlines.average_cloudiness_in_september,
        average_cloudiness_in_october=cloudlines.average_cloudiness_in_october,
        average_cloudiness_in_november=cloudlines.average_cloudiness_in_november,
        average_cloudiness_in_december=cloudlines.average_cloudiness_in_december
    )


def cloudlines_from_repo_to_dto_list(params: list[Cloudlines]) -> list[CloudlinesDto]:
    l = []
    for c in params:
        l.append(CloudlinesDto(
            id=c.id,
            synoptic_index_of_the_station=c.synoptic_index_of_the_station,
            year=c.year,
            type_of_cloudiness=c.type_of_cloudiness,
            average_cloudiness_in_january=c.average_cloudiness_in_january,
            average_cloudiness_in_february=c.average_cloudiness_in_february,
            average_cloudiness_in_march=c.average_cloudiness_in_march,
            average_cloudiness_in_april=c.average_cloudiness_in_april,
            average_cloudiness_in_may=c.average_cloudiness_in_may,
            average_cloudiness_in_june=c.average_cloudiness_in_june,
            average_cloudiness_in_july=c.average_cloudiness_in_july,
            average_cloudiness_in_august=c.average_cloudiness_in_august,
            average_cloudiness_in_september=c.average_cloudiness_in_september,
            average_cloudiness_in_october=c.average_cloudiness_in_october,
            average_cloudiness_in_november=c.average_cloudiness_in_november,
            average_cloudiness_in_december=c.average_cloudiness_in_december
        ))
    return l


def cloudlines_from_dto_to_repo(cloudlines: CloudlinesDto) -> Cloudlines:
    return Cloudlines(
        id=cloudlines.id,
        synoptic_index_of_the_station=cloudlines.synoptic_index_of_the_station,
        year=cloudlines.year,
        type_of_cloudiness=cloudlines.type_of_cloudiness,
        average_cloudiness_in_january=cloudlines.average_cloudiness_in_january,
        average_cloudiness_in_february=cloudlines.average_cloudiness_in_february,
        average_cloudiness_in_march=cloudlines.average_cloudiness_in_march,
        average_cloudiness_in_april=cloudlines.average_cloudiness_in_april,
        average_cloudiness_in_may=cloudlines.average_cloudiness_in_may,
        average_cloudiness_in_june=cloudlines.average_cloudiness_in_june,
        average_cloudiness_in_july=cloudlines.average_cloudiness_in_july,
        average_cloudiness_in_august=cloudlines.average_cloudiness_in_august,
        average_cloudiness_in_september=cloudlines.average_cloudiness_in_september,
        average_cloudiness_in_october=cloudlines.average_cloudiness_in_october,
        average_cloudiness_in_november=cloudlines.average_cloudiness_in_november,
        average_cloudiness_in_december=cloudlines.average_cloudiness_in_december
    )
