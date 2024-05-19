from typing import Annotated

from fastapi import status, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from starlette.responses import JSONResponse

from internal.dto import Token, UserDto
from internal.usecase.auth import UserUseCase
from datetime import timedelta

from internal.usecase.auth.auth import create_access_token
from internal.usecase.auth.s_constant import ACCESS_TOKEN_EXPIRE_MINUTES


class ApplicationUserService(object):
    def __init__(
            self,
    ):
        self.user_uc = UserUseCase()

    def authenticate_user(self, username: str, password: str):
        try:

            user = self.user_uc.authenticate_user(username, password)
            if not user:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Incorrect username or password",
                    headers={"WWW-Authenticate": "Bearer"},
                )
            return user
        except Exception as e:
            print(f"ERROR ::: ApplicationAuth -> authenticate_user: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Internal server error"
            )

    # def create_access_token(self, data: dict, expires_delta: timedelta | None = None):
    #     try:
    #         return self.user_uc.create_access_token(data, expires_delta)
    #     except Exception as e:
    #         print(f"ERROR ::: ApplicationAuth -> create_access_token: {e}")
    #         raise HTTPException(
    #             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    #             detail="Internal server error"
    #         )

    def login_for_access_token(self,
                               form_data,
                               ) -> Token:
        try:
            user = self.user_uc.authenticate_user(form_data.username, form_data.password)
            if not user:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Incorrect username or password",
                    headers={"WWW-Authenticate": "Bearer"},
                )
            access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
            access_token = create_access_token(
                data={"sub": user.username}, expires_delta=access_token_expires
            )
            return Token(access_token=access_token, token_type="bearer")
        except Exception as e:
            print(f"ERROR ::: ApplicationAuth -> login_for_access_token: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Internal server error"
            )

    def get_current_user(self, token: str) -> UserDto:
        try:
            return self.user_uc.get_current_user(token)
        except Exception as e:
            print(f"ERROR ::: ApplicationAuth -> get_current_user: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Internal server error"
            )

    def delete_user(self, user: UserDto):
        try:
            self.user_uc.delete_user(user.username)
            return JSONResponse(content={"message": "User deleted"})
        except Exception as e:
            print(f"ERROR ::: ApplicationAuth -> delete_user: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Internal server error"
            )

    def update_user(self, user: UserDto) -> UserDto:
        try:
            return self.user_uc.update_user(user.username, user.password, user.email)
        except Exception as e:
            print(f"ERROR ::: ApplicationAuth -> update_user: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Internal server error"
            )

    def create_user(self, user: UserDto) -> UserDto:
        try:
            return self.user_uc.create_user(user.username, user.password, user.email)
        except Exception as e:
            print(f"ERROR ::: ApplicationAuth -> create_user: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Internal server error"
            )
