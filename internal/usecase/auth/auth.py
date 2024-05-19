from internal.dto import Token, TokenData, UserDto
from passlib.context import CryptContext
from jose import JWTError, jwt
from internal.entity.user_repository import UserRepository, User
from datetime import datetime, timedelta, timezone
from internal.usecase.auth.s_constant import ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM, SECRET_KEY

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password):
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    """
    Creates access token

    Args:
    data: dict - data
    expires_delta: timedelta | None - expiration time

    Returns:
    str - encoded jwt
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


class UserUseCase(object):
    """
    Class for working with users.
    """

    def __init__(self):
        self.user_repository = UserRepository()

    def authenticate_user(self, username: str, password: str) -> User | bool:
        """
         Authenticates user.

        Args:
        username: str - username
        password: str - password

        Returns:
        User | bool - user or False
        """
        user = self.user_repository.get_user_by_username(username)
        self.user_repository.close()
        if not user:
            return False
        if not verify_password(password, user.hashed_password):
            return False
        return user

    def get_user(self, username: str):
        """
        Gets user by username.

        Args:
        username: str - username

        Returns:
        UserDto - user
        """
        user = self.user_repository.get_user_by_username(username)
        self.user_repository.close()
        return UserDto(
            username=user.username,
            email=user.email,
            disable=user.disable
        )

    def create_user(self, username: str, password: str, email: str):
        """
        Creates user.

        Args:
        username: str - username
        password: str - password
        email: str - email

        Returns:
        UserDto - user
        """
        hashed_password = get_password_hash(password)
        self.user_repository.add_user(username, hashed_password, email)
        self.user_repository.close()
        return UserDto(
            username=username,
            email=email,
            disable=False
        )

    def get_current_user(self, token: str) -> UserDto | None:
        """
        Gets current user.

        Args:
        token: str - token

        Returns:
        UserDto | None - user or None
        """
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username: str = payload.get("sub")
            if username is None:
                return None
            token_data = TokenData(username=username)
        except JWTError:
            raise None
        user = self.user_repository.get_user_by_username(username=token_data.username)
        self.user_repository.close()
        if user is None:
            raise None
        return user

    def delete_user(self, username: str):
        """
        Deletes user by username.

        Args:
        username: str - username
        """
        self.user_repository.delete_user_by_username(username)
        self.user_repository.close()

    def update_user(self, username: str, password: str, email: str) -> UserDto:
        """
        Updates user by username.

        Args:
        username: str - username
        password: str - password
        email: str - email

        Returns:
        UserDto - user
        """
        hashed_password = get_password_hash(password)
        self.user_repository.update_user(username, hashed_password, email)
        self.user_repository.close()
        return UserDto(
            username=username,
            email=email,
            disable=False
        )
