from fastapi import APIRouter

from . import nsi, health, middleware, graph_algos, user

router = APIRouter()
router.include_router(
    nsi.router,
    prefix='/nsi',
    tags=['nsi'],
)
router.include_router(
    health.router,
    prefix='/health',
    tags=['nsi'],
)

router.include_router(
    graph_algos.router,
    prefix='/graph',
    tags=['graph'],
)

router.include_router(
    user.router,
    prefix='/user',
    tags=['user'],
)