from typing import Any

from starlette.responses import JSONResponse

from internal.entity.platform_ca import PlatformCARepository, PlatformCA
from internal.dto import PlatformCADto, ById
from fastapi import status, HTTPException, Depends
from internal.usecase.converters import platform_ca_from_repo_to_dto, platform_ca_from_repo_to_dto_list, \
    platform_ca_from_dto_to_repo


class ApplicationPlatformCAService(object):
    def __init__(
            self,
    ):
        self.repository = PlatformCARepository()

    def add_platform_ca(self, platform_ca: PlatformCADto) -> JSONResponse:
        try:
            platform_ca_repo = platform_ca_from_dto_to_repo(platform_ca)
            self.repository.add_platform_ca(platform_ca_repo)
            return JSONResponse(status_code=status.HTTP_200_OK, content={"success": True})
        except Exception as e:
            print(f"ERROR ::: ApplicationPlatfromCA -> add_platform_ca: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Internal server error",
            )

    def get_platform_ca_by_id(self, in_id: int) -> JSONResponse | PlatformCADto:
        try:
            platform_ca = self.repository.get_platform_ca_by_id(in_id)
            if not platform_ca:
                return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,
                                    content={"success": False, "description": "Platform CA not found"})
            platform_ca_dto = platform_ca_from_repo_to_dto(platform_ca)
            return platform_ca_dto
        except Exception as e:
            print(f"ERROR ::: ApplicationPlatfromCA -> get_platform_ca_by_id: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Internal server error",
            )

    def get_all_platform_ca(self) -> JSONResponse | Any:
        try:
            platform_ca = self.repository.get_all_platform_ca()
            if not platform_ca:
                return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,
                                    content={"success": False, "description": "Platform CA not found"})
            platform_ca_dto = platform_ca_from_repo_to_dto_list(platform_ca)
            return {"data": platform_ca_dto}
        except Exception as e:
            print(f"ERROR ::: ApplicationPlatfromCA -> get_all_platform_ca: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Internal server error",
            )

    def update_platform_ca(self, platform_ca: PlatformCADto) -> JSONResponse:
        try:
            platform_ca_repo = platform_ca_from_dto_to_repo(platform_ca)
            self.repository.update_platform_ca(platform_ca_repo)
            return JSONResponse(status_code=status.HTTP_200_OK, content={"success": True})
        except Exception as e:
            print(f"ERROR ::: ApplicationPlatfromCA -> update_platform_ca: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Internal server error",
            )

    def delete_platform_ca(self, in_id: int) -> JSONResponse:
        try:
            self.repository.delete_platform_ca(in_id)
            return JSONResponse(status_code=status.HTTP_200_OK, content={"success": True})
        except Exception as e:
            print(f"ERROR ::: ApplicationPlatfromCA -> delete_platform_ca: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Internal server error",
            )