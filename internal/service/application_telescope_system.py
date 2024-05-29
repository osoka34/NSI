from typing import Any

from starlette.responses import JSONResponse

from internal.entity.camera_characteristics_repository import TelescopeSystem, TelescopeSystemRepository
from internal.dto import TelescopeSystemDto, ById
from fastapi import status, HTTPException, Depends
from internal.usecase.converters import telescope_system_from_repo_to_dto_list, telescope_system_from_repo_to_dto, \
    telescope_system_from_dto_to_repo


class ApplicationTelescopeSystemService(object):
    def __init__(
            self,
    ):
        self.repository = TelescopeSystemRepository()

    def get_telescope_system_by_id(self, in_id: int) -> JSONResponse | TelescopeSystemDto:
        try:
            telescope_system = self.repository.get_telescope_system_by_id(in_id)
            if not telescope_system:
                return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,
                                    content={"success": False, "description": "Telescope system not found"})
            telescope_system_dto = telescope_system_from_repo_to_dto(telescope_system)
            return telescope_system_dto
        except Exception as e:
            print(f"ERROR ::: ApplicationGroundPoints -> get_telescope_system_by_id: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Internal server error",
            )

    def get_all_telescope_system(self) -> JSONResponse | Any:
        try:
            telescope_system = self.repository.get_all_telescope_systems()
            if not telescope_system:
                return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,
                                    content={"success": False, "description": "Telescope system not found"})
            telescope_system_dto = telescope_system_from_repo_to_dto_list(telescope_system)
            return {"data": telescope_system_dto}
        except Exception as e:
            print(f"ERROR ::: ApplicationGroundPoints -> get_all_telescope_system: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Internal server error",
            )

    def add_telescope_system(self, telescope_system: TelescopeSystemDto) -> JSONResponse:
        try:
            telescope_system_repo = telescope_system_from_dto_to_repo(telescope_system)
            self.repository.add_telescope_system(telescope_system_repo)
            return JSONResponse(status_code=status.HTTP_200_OK, content={"success": True})
        except Exception as e:
            print(f"ERROR ::: ApplicationGroundPoints -> add_telescope_system: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Internal server error",
            )

    def update_telescope_system(self, telescope_system: TelescopeSystemDto) -> JSONResponse:
        try:
            telescope_system_repo = telescope_system_from_dto_to_repo(telescope_system)
            self.repository.update_telescope_system(telescope_system_repo)
            return JSONResponse(status_code=status.HTTP_200_OK, content={"success": True})
        except Exception as e:
            print(f"ERROR ::: ApplicationGroundPoints -> update_telescope_system: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Internal server error",
            )

    def delete_telescope_system(self, in_id: int) -> JSONResponse:
        try:
            self.repository.delete_telescope_system_by_id(in_id)
            return JSONResponse(status_code=status.HTTP_200_OK, content={"success": True})
        except Exception as e:
            print(f"ERROR ::: ApplicationGroundPoints -> delete_telescope_system: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Internal server error",
            )
