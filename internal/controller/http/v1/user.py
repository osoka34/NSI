from typing import Annotated, Union, List

from fastapi import APIRouter, Depends, Body
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from starlette.responses import JSONResponse

from internal.dto import UserDto, Token
from internal.dto.model_auth import CREATE_USER_EXAMPLE, UPDATE_USER_EXAMPLE
from internal.service import ApplicationUserService

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="v1/user/token")

@router.post('/create_user')
async def create_user(
        dto: UserDto = Body(..., examples=CREATE_USER_EXAMPLE),
        application_service: ApplicationUserService = Depends(),
) -> UserDto:
    """
    Create user with all fields
    Args:
    dto (CreateUserRequest): CreateUserRequest
    Returns:
    UserDto - user
    """
    return application_service.create_user(dto)


@router.post('/get_by_token')
async def get_user_by_token(
        token: Annotated[str, Depends(oauth2_scheme)],
        application_service: ApplicationUserService = Depends(),
) -> UserDto:
    """
    Get user
    Args:
    token: str
    Returns:
    UserDto - user
    """
    return application_service.get_current_user(token)


@router.post('/token')
async def get_token(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
        application_service: ApplicationUserService = Depends(),
) -> Token:
    """
    Get token for user

    Returns:
    Access token for user
    """
    return application_service.login_for_access_token(form_data)


@router.post('/update_user', dependencies=[Depends(get_user_by_token)])
async def update_user(
        dto: UserDto = Body(..., example=UPDATE_USER_EXAMPLE),
        application_service: ApplicationUserService = Depends(),
) -> UserDto:
    """
    Update user
    Args:
    dto UserDto - user
    Returns:
    UserDto - user
    """
    return application_service.update_user(dto)


@router.post('/delete_user', dependencies=[Depends(get_user_by_token)])
async def delete_user(
        dto: UserDto,
        application_service: ApplicationUserService = Depends(),
) -> UserDto:
    """
    Delete user
    Args:
    UserDto - user.nickname only needs
    Returns:
    JSONResponse: Default response with bool success and str message
    """
    return application_service.delete_user(dto)