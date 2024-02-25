from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from internal.controller.http.router import api_router
from internal.controller.http.v1 import middleware


def create_app() -> FastAPI:
    """
    Create FastAPI app

    Returns:
    FastAPI app
    """
    app = FastAPI()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )

    app.middleware("http")(middleware.log_requests)

    app.include_router(api_router)
    return app
