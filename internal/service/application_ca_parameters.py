from typing import Any

from starlette.responses import JSONResponse
from fastapi import status, HTTPException, Depends

from internal.entity.ca_parameters import CAParametersRepository, CAParameters, CAPlatformView
from internal.dto import CAParametersDto, CAPlatformViewDto
from internal.usecase.converters import (
    ca_parameters_from_repo_to_dto,
    ca_parameters_from_repo_to_dto_list,
    ca_parameters_from_dto_to_repo,
    ca_platform_view_from_repo_to_dto,
    ca_platform_view_from_repo_to_dto_list
)


class ApplicationCAParametersService(object):
    def __init__(self):
        self.repository = CAParametersRepository()

    def add_ca_parameters(self, ca_parameters: CAParametersDto) -> JSONResponse:
        try:
            ca_parameters_repo = ca_parameters_from_dto_to_repo(ca_parameters)
            self.repository.add_ca_parameters(ca_parameters_repo)
            return JSONResponse(status_code=status.HTTP_200_OK, content={"success": True})
        except Exception as e:
            print(f"ERROR ::: ApplicationCAParameters -> add_ca_parameters: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Internal server error",
            )

    def get_ca_parameters_by_id(self, in_id: int) -> JSONResponse | CAParametersDto:
        try:
            ca_parameters = self.repository.get_ca_parameters_by_id(in_id)
            if not ca_parameters:
                return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,
                                    content={"success": False, "description": "CA Parameters not found"})
            ca_parameters_dto = ca_parameters_from_repo_to_dto(ca_parameters)
            return ca_parameters_dto
        except Exception as e:
            print(f"ERROR ::: ApplicationCAParameters -> get_ca_parameters_by_id: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Internal server error",
            )

    def get_all_ca_parameters(self) -> JSONResponse | Any:
        try:
            ca_parameters = self.repository.get_all_ca_parameters()
            if not ca_parameters:
                return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,
                                    content={"success": False, "description": "CA Parameters not found"})
            ca_parameters_dto = ca_parameters_from_repo_to_dto_list(ca_parameters)
            return {"data": ca_parameters_dto}
        except Exception as e:
            print(f"ERROR ::: ApplicationCAParameters -> get_all_ca_parameters: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Internal server error",
            )

    def update_ca_parameters(self, ca_parameters: CAParametersDto) -> JSONResponse:
        try:
            ca_parameters_repo = ca_parameters_from_dto_to_repo(ca_parameters)
            self.repository.update_ca_parameters(ca_parameters_repo.id, ca_parameters_repo)
            return JSONResponse(status_code=status.HTTP_200_OK, content={"success": True})
        except Exception as e:
            print(f"ERROR ::: ApplicationCAParameters -> update_ca_parameters: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Internal server error",
            )

    def delete_ca_parameters(self, in_id: int) -> JSONResponse:
        try:
            self.repository.delete_ca_parameters(in_id)
            return JSONResponse(status_code=status.HTTP_200_OK, content={"success": True})
        except Exception as e:
            print(f"ERROR ::: ApplicationCAParameters -> delete_ca_parameters: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Internal server error",
            )

    def get_all_ca_platform_view(self) -> JSONResponse | Any:
        try:
            ca_platform_views = self.repository.get_all_ca_platform_view()
            if not ca_platform_views:
                return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,
                                    content={"success": False, "description": "CA Platform View not found"})
            ca_platform_view_dto = ca_platform_view_from_repo_to_dto_list(ca_platform_views)
            return {"data": ca_platform_view_dto}
        except Exception as e:
            print(f"ERROR ::: ApplicationCAParameters -> get_ca_platform_view_by_id: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Internal server error",
            )

    def get_all_by_id_ca_platform_view(self, ca_id: int) -> JSONResponse | Any:
        try:
            ca_platform_view = self.repository.get_all_by_id_ca_platform_view(ca_id)
            if not ca_platform_view:
                return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,
                                    content={"success": False, "description": "CA Platform View not found"})
            ca_platform_view_dto = ca_platform_view_from_repo_to_dto_list(ca_platform_view)
            return {"data": ca_platform_view_dto}
        except Exception as e:
            print(f"ERROR ::: ApplicationCAParameters -> get_all_ca_platform_view: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Internal server error",
            )
