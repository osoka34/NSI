from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class UserDto(BaseModel):
    username: str
    email: str | None = None
    password: str | None = None
    disabled: bool | None = None


CREATE_USER_EXAMPLE = [
    {
        "username": "test",
        "email": "test@mail.com",
        "password": "test",
        "disabled": False,
    },
]

UPDATE_USER_EXAMPLE = [
    {
        "username": "test",
        "email": "new@mail.com",
    },
]

DELETE_USER_EXAMPLE = [
    {
        "username": "test",
    }
]
