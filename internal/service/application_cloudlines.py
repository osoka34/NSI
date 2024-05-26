from starlette.responses import JSONResponse

from internal.entity.cloudlines_repository import CloudlinesRepository, Cloudlines
from internal.dto import CloudlinesDto, ById
from fastapi import status, HTTPException, Depends
from internal.usecase.converters import cloudlines_from_repo_to_dto, cloudlines_from_repo_to_dto_list, \
    cloudlines_from_dto_to_repo


class ApplicationCloudlinesService(object):
    def __init__(
            self,
    ):
        self.repository = CloudlinesRepository()

    def get_cloudlines_by_id(self, in_id: int) -> JSONResponse:
        try:
            cloudlines = self.repository.get_cloudlines_by_id(in_id)
            if not cloudlines:
                return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,
                                    content={"success": False, "description": "Cloudline not found"})
            cloudlines_dto = cloudlines_from_repo_to_dto(cloudlines)
            return JSONResponse(status_code=status.HTTP_200_OK, content=cloudlines_dto)
        except Exception as e:
            print(f"ERROR ::: ApplicationCloudlines -> get_cloudlines_by_id: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_ERROR,
                detail="Internal server error",
            )

    def get_all_cloudlines(self) -> JSONResponse:
        try:
            cloudlines = self.repository.get_all_cloudlines()
            if not cloudlines:
                return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,
                                    content={"success": False, "description": "Cloudlines not found"})
            cloudlines_dto = cloudlines_from_repo_to_dto_list(cloudlines)
            return JSONResponse(status_code=status.HTTP_200_OK, content=cloudlines_dto)
        except Exception as e:
            print(f"ERROR ::: ApplicationCloudlines -> get_all_cloudlines: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_ERROR,
                detail="Internal server error",
            )

    def add_cloudlines(self, cloudlines: CloudlinesDto) -> JSONResponse:
        try:
            cloudlines_repo = cloudlines_from_dto_to_repo(cloudlines)
            self.repository.add_cloudlines(cloudlines_repo)
            return JSONResponse(status_code=status.HTTP_200_OK, content=cloudlines)
        except Exception as e:
            print(f"ERROR ::: ApplicationCloudlines -> add_cloudlines: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_ERROR,
                detail="Internal server error",
            )

    def update_cloudlines(self, cloudlines: CloudlinesDto) -> JSONResponse:
        try:
            cloudlines_repo = cloudlines_from_dto_to_repo(cloudlines)
            self.repository.update_cloudlines(cloudlines_repo)
            return JSONResponse(status_code=status.HTTP_200_OK, content=cloudlines)
        except Exception as e:
            print(f"ERROR ::: ApplicationCloudlines -> update_cloudlines: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_ERROR,
                detail="Internal server error",
            )

    def delete_cloudlines(self, in_id: int) -> JSONResponse:
        try:
            self.repository.delete_cloudlines_by_id(in_id)
            return JSONResponse(status_code=status.HTTP_200_OK, content={"success": True})
        except Exception as e:
            print(f"ERROR ::: ApplicationCloudlines -> delete_cloudlines: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_ERROR,
                detail="Internal server error",
            )
