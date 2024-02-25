from internal.entity.repository import Repository
from internal.entity.repository import RequestLogs
from fastapi import Request
from datetime import datetime


async def log_requests(request: Request, call_next):
    """
    Middleware for logging requests.
    Logs the request to the database.

    Args:
    request: Request - request object
    call_next: function - next middleware function or the request handler
    """

    repository = Repository()
    request_logs: RequestLogs = RequestLogs()
    request_logs.request_type = request.method
    request_logs.request_path = request.url.path
    request_logs.request_body = str(await request.body())
    request_logs.request_ip = request.client.host
    request_logs.request_user_agent = request.headers["user-agent"]
    request_logs.request_host = request.headers["host"]
    request_logs.request_query = str(request.query_params)
    request_logs.request_time = int(datetime.now().timestamp())
    repository.add_request_logs(request_logs)
    repository.close()

    return await call_next(request)
