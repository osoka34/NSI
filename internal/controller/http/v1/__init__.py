from fastapi import APIRouter

from . import (nsi, health, middleware, graph_algos, user,
               cloudlines, cloud_station, ground_points,
               named_const, telescope_system, platform_ca,
               project)

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

router.include_router(
    cloudlines.router,
    prefix='/cloudlines',
    tags=['cloudlines'],
)

router.include_router(
    cloud_station.router,
    prefix='/cloud_station',
    tags=['cloud_station'],
)

router.include_router(
    ground_points.router,
    prefix='/ground_points',
    tags=['ground_points'],
)

router.include_router(
    named_const.router,
    prefix='/named_const',
    tags=['named_const'],
)

router.include_router(
    telescope_system.router,
    prefix='/telescope_system',
    tags=['telescope_system'],
)

router.include_router(
    platform_ca.router,
    prefix='/platform_ca',
    tags=['platform_ca'],
)


router.include_router(
    project.router,
    prefix='/project',
    tags=['project'],
)

