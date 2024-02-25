from typing import Any

from starlette.responses import JSONResponse

from internal.entity.repository import Repository
from internal.usecase.parser import InfoParser
from internal.dto import LoadNSIRequest, DefaultResponse, GetNSIRequest, GetNSIResponse
from internal.service import HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_500_INTERNAL_ERROR
from internal.usecase.utils import validate_dtype, generate_uuid


class ApplicationService(object):
    def __init__(
            self,
    ):
        self.repository = Repository()
        self.parser = InfoParser()

    def load_nsi_data(self, req: LoadNSIRequest) -> JSONResponse:
        """
        Loads NSI data to the database.
        Downloads the file from the web, parses it and adds the data to the database.

        Args:
        req: LoadNSIRequest - request object

        Returns:
        JSONResponse - response object
        """

        if not validate_dtype(req.data_type):
            print("Invalid data type")
            return JSONResponse(
                content=DefaultResponse(
                    success=False,
                    description="Invalid data type"
                ).dict(),
                status_code=HTTP_400_BAD_REQUEST,
            )

        if req.download_link == "":
            return JSONResponse(
                content=DefaultResponse(success=False, description="Download link is empty").dict(),
                status_code=HTTP_400_BAD_REQUEST,
            )

        filename = generate_uuid()
        self.parser.download_from_web(req.download_link, filename)
        data: list[dict] = self.parser.parse(filename, req.data_type)
        self.repository.add_nsi_data_list(data[:10])
        self.parser.delete_file(filename)
        self.repository.close()
        return JSONResponse(
            content=DefaultResponse(success=True, description="Data loaded").dict(),
            status_code=HTTP_200_OK,
        )

    def get_nsi_data(self, req: GetNSIRequest) -> JSONResponse | dict[str, Any]:
        """
        Gets NSI data from the database and returns a JSON object response.

        Args:
        req: GetNSIRequest - request object

        Returns:
        JSONResponse - response object
        """
        if not validate_dtype(req.data_type):
            return JSONResponse(
                content=DefaultResponse(
                    success=False,
                    description="Invalid data type"
                ).dict(),
                status_code=HTTP_400_BAD_REQUEST,
            )

        data = self.repository.get_nsi_data_view(req.data_type, req.limit)
        objects_list = [obj.__dict__ for obj in data]
        cleaned_data_list = [{k: v for k, v in obj.items() if k != '_sa_instance_state' and v != ''} for obj in
                             objects_list]
        return {
                "data": cleaned_data_list,
                "success": True,
                "description": "Data loaded"
            }