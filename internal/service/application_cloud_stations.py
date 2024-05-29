from typing import Any

from starlette.responses import JSONResponse

from internal.entity.cloud_stations_repository import CloudStation, CloudStationRepository
from internal.dto import CloudStationDto, ById
from fastapi import status, HTTPException, Depends
from internal.usecase.converters import cloud_station_from_dto_to_repo, cloud_station_from_repo_to_dto, \
    cloud_station_from_repo_to_dto_list


class ApplicationCloudStationService(object):
    def __init__(
            self,
    ):
        self.repository = CloudStationRepository()

    def get_cloud_station_by_id(self, in_id: int) -> JSONResponse | CloudStationDto:
        try:
            cloud_station = self.repository.get_cloud_station_by_id(in_id)
            if not cloud_station:
                return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,
                                    content={"success": False, "description": "Cloud station not found"})
            cloud_station_dto = cloud_station_from_repo_to_dto(cloud_station)
            return cloud_station_dto
        except Exception as e:
            print(f"ERROR ::: ApplicationGroundPoints -> get_cloud_station_by_id: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Internal server error",
            )

    def get_all_cloud_station(self) -> JSONResponse | Any:
        try:
            cloud_station = self.repository.get_all_cloud_stations()
            if not cloud_station:
                return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,
                                    content={"success": False, "description": "Cloud station not found"})
            cloud_station_dto = cloud_station_from_repo_to_dto_list(cloud_station)
            return {"data": cloud_station_dto}
        except Exception as e:
            print(f"ERROR ::: ApplicationGroundPoints -> get_all_cloud_station: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Internal server error",
            )

    def add_cloud_station(self, cloud_station: CloudStationDto) -> JSONResponse:
        try:
            cloud_station_repo = cloud_station_from_dto_to_repo(cloud_station)
            self.repository.add_cloud_station(cloud_station_repo)
            return JSONResponse(status_code=status.HTTP_200_OK, content={"success": True})
        except Exception as e:
            print(f"ERROR ::: ApplicationGroundPoints -> add_cloud_station: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Internal server error",
            )

    def update_cloud_station(self, cloud_station: CloudStationDto) -> JSONResponse:
        try:
            cloud_station_repo = cloud_station_from_dto_to_repo(cloud_station)
            self.repository.update_cloud_station(cloud_station_repo)
            return JSONResponse(status_code=status.HTTP_200_OK, content={"success": True})
        except Exception as e:
            print(f"ERROR ::: ApplicationGroundPoints -> update_cloud_station: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Internal server error",
            )

    def delete_cloud_station(self, in_id: int) -> JSONResponse:
        try:
            self.repository.delete_cloud_station_by_id(in_id)
            return JSONResponse(status_code=status.HTTP_200_OK, content={"success": True})
        except Exception as e:
            print(f"ERROR ::: ApplicationGroundPoints -> delete_cloud_station: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Internal server error",
            )
