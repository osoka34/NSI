from internal.usecase.utils import get_session

from sqlalchemy.orm import Session
from internal.entity.cloudlines_repository.model import Cloudlines

class CloudlinesRepository(object):
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

    def add_cloudlines(self, data: Cloudlines) -> None:
        """
        Adds data to the database.
        Converts dictionary to Cloudlines instance and adds it to the database.

        Args:
        data: Cloudlines
        """
        try:
            self.session.add(data)
            self.session.commit()
        except Exception as e:
            print(f"Error occurred while adding data to the database: {e}")

    def get_cloudlines_by_id(self, id: int) -> Cloudlines:
        """
        Gets data from the database by id.

        Args:
        id: int - id of the data

        Returns:
        Cloudlines - data from the database
        """
        try:
            return self.session.query(Cloudlines).filter(Cloudlines.id == id).first()
        except Exception as e:
            print(f"Error occurred while getting data from the database: {e}")

    def get_all_cloudlines(self) -> list[Cloudlines]:
        """
        Gets all data from the database.

        Returns:
        list[Cloudlines] - list of data from the database
        """
        try:
            return self.session.query(Cloudlines).all()
        except Exception as e:
            print(f"Error occurred while getting data from the database: {e}")

    def delete_cloudlines_by_id(self, id: int) -> None:
        """
        Deletes data from the database by id.

        Args:
        id: int - id of the data
        """
        try:
            self.session.query(Cloudlines).filter(Cloudlines.id == id).delete()
            self.session.commit()
        except Exception as e:
            print(f"Error occurred while deleting data from the database: {e}")

    def update_cloudlines(self, data: Cloudlines) -> None:
        """
        Updates data in the database.

        Args:
        data: Cloudlines
        """
        try:
            self.session.query(Cloudlines).filter(Cloudlines.id == data.id).update(data)
            self.session.commit()
        except Exception as e:
            print(f"Error occurred while updating data in the database: {e}")