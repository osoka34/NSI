from fastapi import APIRouter

from internal.controller.http import v1


"""
API Router

This module is used to define the API router for the application.
"""


api_router = APIRouter()
api_router.include_router(v1.router, prefix='/v1')