from typing import Any

from starlette.responses import JSONResponse

from internal.entity.repository import Repository
from internal.usecase.parser import InfoParser
from internal.dto import LoadNSIRequest, DefaultResponse, GetNSIRequest, NSI_BAD_REQUEST
from internal.service import HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_500_INTERNAL_ERROR, INTERNAL_ERROR
from internal.usecase.utils import validate_dtype, generate_uuid


class ApplicationNSIService(object):
    def __init__(
            self,
    ):
        """
        ApplicationNSIService constructor

        repository: Repository - repository object
        parser: InfoParser - parser object
        """
        self.repository = Repository()
        self.parser = InfoParser()

    def load_nsi_data(self, req: LoadNSIRequest) -> JSONResponse:
        """
        Loads NSI data to the database.
        Downloads the file from the web, parses it and adds the data to the database.

        Args:
        req: LoadNSIRequest - request object

        Example:
            {
                "download_link": "https://www.example.com/data.txt",
                "data_type": 1
            }

        Returns:
        JSONResponse - response object

        Examples:
            Success 200:
            {
                "success": true,
                "description": "Data loaded"
            }
            Failure 400:
            {
                "success": false,
                "description": "Download link is empty"
            }
            Failure 500:
            {
                "success": false,
                "description": "Internal server error"
            }
        """
        try:
            if not validate_dtype(req.data_type):
                return NSI_BAD_REQUEST

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
        except Exception as e:
            print(f"ERROR ::: ApplicationNSIService -> load_nsi_data: {e}")
            return INTERNAL_ERROR

    def get_nsi_data(self, req: GetNSIRequest) -> JSONResponse | dict[str, Any]:
        """
        Gets NSI data from the database and returns a JSON object response.

        Args:
        req: GetNSIRequest - request object

        Example:
            {
                "data_type": 1,
                "limit": 10
            }

        Returns:
        JSONResponse - response object

        Examples:
            Success 200:
            {
                "data": [
                    {
                        "id": 1,
                        "value1": val,
                        "value2": val,
                    }
                ],
                "success": true,
                "description": "Data loaded"
            }
            Failure 400:
            {
                "success": false,
                "description": "Data type is not valid"
            }
            Failure 500:
            {
                "success": false,
                "description": "Internal server error"
            }
        """
        try:
            if not validate_dtype(req.data_type):
                return NSI_BAD_REQUEST

            data = self.repository.get_nsi_data_view(req.data_type, req.limit)
            objects_list = [obj.__dict__ for obj in data]
            cleaned_data_list = [{k: v for k, v in obj.items() if k != '_sa_instance_state' and v != ''} for obj in
                                 objects_list]
            return {
                    "data": cleaned_data_list,
                    "success": True,
                    "description": "Data loaded"
                }
        except Exception as e:
            print(f"ERROR ::: ApplicationNSIService -> get_nsi_data: {e}")
            return INTERNAL_ERROR
