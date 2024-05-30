from internal.usecase.utils import get_session

from sqlalchemy.orm import Session
from internal.entity.named_constants_repository.model import NamesConstants


class NamesConstantsRepository(object):
    """
    Class for working with the database.

    Attributes:
    session: Session - connection to the database
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

    def add_named_constants(self, data: NamesConstants) -> None:
        """
        Adds data to the database.
        Converts dictionary to NamesConstants instance and adds it to the database.

        Args:
        data: NamesConstants
        """
        try:
            self.session.add(data)
            self.session.commit()
        except Exception as e:
            print(f"Error occurred while adding data to the database: {e}")

    def get_named_constants_by_id(self, id: int) -> NamesConstants:
        """
        Gets data from the database by id.

        Args:
        id: int - id of the data

        Returns:
        NamesConstants - data from the database
        """
        try:
            return self.session.query(NamesConstants).filter(NamesConstants.id == id).first()
        except Exception as e:
            print(f"Error occurred while getting data from the database: {e}")
            return None

    def get_all_named_constants(self) -> list[NamesConstants]:
        """
        Gets all data from the database.

        Returns:
        list[NamesConstants] - all data from the database
        """
        try:
            return self.session.query(NamesConstants).all()
        except Exception as e:
            print(f"Error occurred while getting data from the database: {e}")
            return []

    def delete_named_constants_by_id(self, id: int) -> None:
        """
        Deletes data from the database by id.

        Args:
        id: int - id of the data
        """
        try:
            self.session.query(NamesConstants).filter(NamesConstants.id == id).delete()
            self.session.commit()
        except Exception as e:
            print(f"Error occurred while deleting data from the database: {e}")


    def update_named_constants(self, data: NamesConstants) -> None:
        """
        Updates data in the database.

        Args:
        data: NamesConstants
        """
        try:
            self.session.query(NamesConstants).filter(NamesConstants.id == data.id).update(data.to_dict())
            self.session.commit()
        except Exception as e:
            print(f"Error occurred while updating data in the database: {e}")



