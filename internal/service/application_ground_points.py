from typing import Any

from starlette.responses import JSONResponse

from internal.entity.ground_points_repository import GroundPointsRepository, GroundPoints
from internal.dto import GroundPointsDto, ById
from fastapi import status, HTTPException, Depends
from internal.usecase.converters import ground_p_from_repo_to_dto, ground_p_from_repo_to_dto_list, ground_p_from_dto_to_repo


class ApplicationGroundPointsService(object):
    def __init__(
            self,
    ):
        self.repository = GroundPointsRepository()

    def get_ground_points_by_id(self, in_id: int) -> JSONResponse | GroundPointsDto:
        try:
            ground_points = self.repository.get_ground_points_by_id(in_id)
            if not ground_points:
                return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,
                                    content={"success": False, "description": "Ground point not found"})
            ground_points_dto = ground_p_from_repo_to_dto(ground_points)
            return ground_points_dto
        except Exception as e:
            print(f"ERROR ::: ApplicationGroundPoints -> get_ground_points_by_id: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Internal server error",
            )

    def get_all_ground_points(self) -> JSONResponse | Any:
        try:
            ground_points = self.repository.get_all_ground_points()
            if not ground_points:
                return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,
                                    content={"success": False, "description": "Ground points not found"})
            ground_points_dto = ground_p_from_repo_to_dto_list(ground_points)
            return {"data": ground_points_dto}
        except Exception as e:
            print(f"ERROR ::: ApplicationGroundPoints -> get_all_ground_points: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Internal server error",
            )

    def add_ground_points(self, ground_points: GroundPointsDto) -> JSONResponse:
        try:
            ground_points_repo = ground_p_from_dto_to_repo(ground_points)
            self.repository.add_ground_points(ground_points_repo)
            return JSONResponse(status_code=status.HTTP_200_OK, content={"success": True})
        except Exception as e:
            print(f"ERROR ::: ApplicationGroundPoints -> add_ground_points: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Internal server error",
            )

    def update_ground_points(self, ground_points: GroundPointsDto) -> JSONResponse:
        try:
            ground_points_repo = ground_p_from_dto_to_repo(ground_points)
            self.repository.update_ground_points(ground_points_repo)
            return JSONResponse(status_code=status.HTTP_200_OK, content={"success": True})
        except Exception as e:
            print(f"ERROR ::: ApplicationGroundPoints -> update_ground_points: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Internal server error",
            )

    def delete_ground_points(self, in_id: int) -> JSONResponse:
        try:
            self.repository.delete_ground_points_by_id(in_id)
            return JSONResponse(status_code=status.HTTP_200_OK, content={"success": True})
        except Exception as e:
            print(f"ERROR ::: ApplicationGroundPoints -> delete_ground_points: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Internal server error",
            )



