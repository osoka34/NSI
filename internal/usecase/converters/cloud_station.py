from internal.entity.cloud_stations_repository import CloudStation
from internal.dto import CloudStationDto



# class CloudStationDto(BaseModel):
#     id: int
#     index_vmo: int
#     station_name: str
#     latitude: str
#     longitude: str
#     height_homeopost: int
#     collect_from: int
#     note: str

def cloud_station_from_repo_to_dto(cloud_station: CloudStation) -> CloudStationDto:
    return CloudStationDto(
        id=cloud_station.id,
        index_vmo=cloud_station.index_vmo,
        station_name=cloud_station.station_name,
        latitude=cloud_station.latitude,
        longitude=cloud_station.longitude,
        height_homeopost=cloud_station.height_homeopost,
        collect_from=cloud_station.collect_from,
        note=cloud_station.note
    )


def cloud_station_from_repo_to_dto_list(params: list[CloudStation]) -> list[CloudStationDto]:
    l = []
    for c in params:
        l.append(CloudStationDto(
            id=c.id,
            index_vmo=c.index_vmo,
            station_name=c.station_name,
            latitude=c.latitude,
            longitude=c.longitude,
            height_homeopost=c.height_homeopost,
            collect_from=c.collect_from,
            note=c.note
        ))
    return l


def cloud_station_from_dto_to_repo(cloud_station: CloudStationDto) -> CloudStation:
    return CloudStation(
        id=cloud_station.id,
        index_vmo=cloud_station.index_vmo,
        station_name=cloud_station.station_name,
        latitude=cloud_station.latitude,
        longitude=cloud_station.longitude,
        height_homeopost=cloud_station.height_homeopost,
        collect_from=cloud_station.collect_from,
        note=cloud_station.note
    )