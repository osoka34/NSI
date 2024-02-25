# from datetime import datetime
# from typing import Dict, List, Any
#
# from fastapi import FastAPI, Request
# from fastapi.responses import JSONResponse
# from starlette.responses import JSONResponse
#
# from repository.model import RequestLogs
# from repository.repository import Repository
# from handler.model import LoadNSIRequest, LoadNSIResponse, GetNSIRequest, GetNSIResponse
# from parser.parser import InfoParser
# from parser.s_constant import TEMP_FILE
# import parser.s_constant
# from fastapi.encoders import jsonable_encoder
# from parser.s_constant import D_TYPE_EOP, D_TYPE_SPACE_ENV, D_TYPE_C20
#
# app: FastAPI = FastAPI()
#
# db_url = 'postgresql://postgres:postgres@my_postgres_container:5432/postgres'
#
#
# @app.middleware("http")
# async def log_requests(request: Request, call_next):
#     """
#     Middleware for logging requests.
#     Logs the request to the database.
#
#     Args:
#     request: Request - request object
#     call_next: function - next middleware function or the request handler
#     """
#
#     repository = Repository(db_url)
#
#     request_logs: RequestLogs = RequestLogs()
#     request_logs.request_type = request.method
#     request_logs.request_path = request.url.path
#     request_logs.request_body = str(await request.body())
#     request_logs.request_ip = request.client.host
#     request_logs.request_user_agent = request.headers["user-agent"]
#     request_logs.request_host = request.headers["host"]
#     request_logs.request_query = str(request.query_params)
#     request_logs.request_time = int(datetime.now().timestamp())
#     repository.add_request_logs(request_logs)
#     repository.close()
#
#     return await call_next(request)
#
#
# @app.post("/load_nsi_data")
# async def load_nsi_data(req: LoadNSIRequest) -> JSONResponse:
#     """
#     Loads NSI data to the database.
#     Downloads the file from the web, parses it and adds the data to the database.
#
#     Args:
#     req: LoadNSIRequest - request object
#
#     Returns:
#     JSONResponse - response object
#     """
#
#     try:
#         parserNSI = InfoParser(req.data_type)
#     except Exception as e:
#         response = LoadNSIResponse(success=False, description=str(e))
#         json_data = jsonable_encoder(response)
#         return JSONResponse(json_data)
#
#     if req.download_link == "":
#         response = LoadNSIResponse(success=False, description="Download link is empty")
#         json_data = jsonable_encoder(response)
#         return JSONResponse(json_data)
#
#     repository: Repository = Repository(db_url)
#     # TODO add uuid to filename
#     parserNSI.download_from_web(req.download_link, TEMP_FILE)
#     data: list[dict] = parserNSI.parse(TEMP_FILE)
#     repository.add_nsi_data_list(data[:10])
#     parserNSI.delete_file(TEMP_FILE)
#     repository.close()
#     response = LoadNSIResponse(success=True, description="OK")
#     json_data = jsonable_encoder(response)
#
#     return JSONResponse(json_data)
#
#
# @app.post("/get_nsi_data")
# async def get_nsi_data(req: GetNSIRequest) -> JSONResponse | dict[str, Any]:
#     """
#     Gets NSI data from the database and returns a JSON object response.
#     At first checks the data type and then gets the data from the database.
#
#     Args:
#     req: GetNSIRequest - request object
#
#     Returns:
#     JSONResponse - response object
#     dict[str, Any] - response object
#     """
#     match req.data_type:
#         case parser.s_constant.D_TYPE_EOP:
#             pass
#         case parser.s_constant.D_TYPE_SPACE_ENV:
#             pass
#         case parser.s_constant.D_TYPE_C20:
#             pass
#         case _:
#             response = GetNSIResponse(data=[], success=False, description="Unknown data type")
#             json_data = jsonable_encoder(response)
#             return JSONResponse(json_data)
#
#     repository: Repository = Repository(db_url)
#     data: list[dict] = repository.get_nsi_data_view(req.data_type)
#     repository.close()
#     objects_list = [obj.__dict__ for obj in data]
#     cleaned_data_list = [{k: v for k, v in obj.items() if k != '_sa_instance_state' and v != ''} for obj in objects_list]
#
#     return {"data": cleaned_data_list, "success": True, "description": "OK"}
#

import sys
from pathlib import Path

# BASE_DIR = Path(__file__).resolve().parents[2]
# sys.path.append(str(BASE_DIR))
# print(BASE_DIR)

from internal.app import backend_app  # noqa: E402

app = backend_app()

