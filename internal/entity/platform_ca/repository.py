from internal.usecase.utils import get_session

from sqlalchemy.orm import Session
from internal.entity.platform_ca.model import PlatformCA


class PlatformCARepository(object):
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

    def add_platform_ca(self, data: PlatformCA) -> None:
        """
        Adds data to the database.
        Converts dictionary to PlatformCA instance and adds it to the database.

        Args:
        data: PlatformCA
        """
        try:
            self.session.add(data)
            self.session.commit()
        except Exception as e:
            print(f"Error occurred while adding data to the database: {e}")

    def get_platform_ca_by_id(self, id: int) -> PlatformCA:
        """
        Gets data from the database by id.

        Args:
        id: int - id of the data

        Returns:
        PlatformCA - data from the database
        """
        try:
            return self.session.query(PlatformCA).filter(PlatformCA.id == id).first()
        except Exception as e:
            print(f"Error occurred while getting data from the database: {e}")

    def get_all_platform_ca(self) -> list:
        """
        Gets all data from the database.

        Returns:
        list - all data from the database
        """
        try:
            return self.session.query(PlatformCA).all()
        except Exception as e:
            print(f"Error occurred while getting data from the database: {e}")

    def update_platform_ca(self, id: int, data: PlatformCA) -> None:
        """
        Updates data in the database.

        Args:
        id: int - id of the data
        data: dict - new data
        """
        try:
            self.session.query(PlatformCA).filter(PlatformCA.id == id).update(data.to_dict())
            self.session.commit()
        except Exception as e:
            print(f"Error occurred while updating data in the database: {e}")

    def delete_platform_ca(self, id: int) -> None:
        """
        Deletes data from the database.

        Args:
        id: int - id of the
        """
        try:
            self.session.query(PlatformCA).filter(PlatformCA.id == id).delete()
            self.session.commit()
        except Exception as e:
            print(f"Error occurred while deleting data from the database: {e}")


