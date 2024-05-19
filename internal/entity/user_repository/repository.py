from internal.usecase.utils import get_session
from fastapi import Depends

from internal.entity.repository.model import NSIData, RequestLogs
from sqlalchemy.orm import Session
from internal.entity.user_repository.model import User


class UserRepository(object):
    """
    Class for working with the database.

    """

    def __init__(
            self,
            session: Session = get_session()
    ):
        """
        Constructor for Repository class.
        Creates a connection to the database.

        session: Session - connection to the database
        """
        self.session = session

    def close(self):
        """
        Closes the connection to the database.
        """

        if self.session:
            self.session.close()
            self.session = None

    def add_user(self, username: str, hashed_password: str, email: str) -> None:
        """
        Adds user to the database.

        Args:
        username: str - username
        hashed_password: str - hashed password
        email: str - email
        """
        try:
            user = User(username=username, hashed_password=hashed_password, email=email)
            self.session.add(user)
            self.session.commit()
        except Exception as e:
            print(f"Error occurred while adding user to the database: {e}")

    def get_user_by_username(self, username: str) -> User:
        """
        Gets user by username.

        Args:
        username: str - username

        Returns:
        User - user
        """
        try:
            user = self.session.query(User).filter(User.username == username).first()
            return user
        except Exception as e:
            print(f"Error occurred while getting user by username from the database: {e}")

    def delete_user_by_username(self, username: str) -> None:
        """
        Deletes user by username.

        Args:
        username: str - username
        """
        try:
            user = self.session.query(User).filter(User.username == username).first()
            user.disable = True
            # self.session.delete(user)
            self.session.commit()
        except Exception as e:
            print(f"Error occurred while deleting user by username from the database: {e}")

    def update_user(self, username: str, hashed_password: str, email: str) -> None:
        """
        Updates user by username.

        Args:
        username: str - username
        hashed_password: str - hashed password
        email: str - email
        """
        try:
            user = self.session.query(User).filter(User.username == username).first()
            user.hashed_password = hashed_password
            user.email = email
            self.session.commit()
        except Exception as e:
            print(f"Error occurred while updating user by username from the database: {e}")
