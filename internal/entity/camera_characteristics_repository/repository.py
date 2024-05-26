from internal.usecase.utils import get_session

from sqlalchemy.orm import Session
from internal.entity.camera_characteristics_repository.model import TelescopeSystem

class TelescopeSystemRepository(object):
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

    def add_telescope_system(self, data: TelescopeSystem) -> None:
        """
        Adds data to the database.
        Converts dictionary to TelescopeSystem instance and adds it to the database.

        Args:
        data: TelescopeSystem
        """
        try:
            self.session.add(data)
            self.session.commit()
        except Exception as e:
            print(f"Error occurred while adding data to the database: {e}")

    def get_telescope_system_by_id(self, id: int) -> TelescopeSystem:
        """
        Gets data from the database by id.

        Args:
        id: int - id of the data

        Returns:
        TelescopeSystem - data from the database
        """
        try:
            return self.session.query(TelescopeSystem).filter(TelescopeSystem.id == id).first()
        except Exception as e:
            print(f"Error occurred while getting data from the database: {e}")
            return TelescopeSystem()

    def delete_telescope_system_by_id(self, id: int) -> None:
        """
        Deletes data from the database by id.

        Args:
        id: int - id of the data
        """
        try:
            self.session.query(TelescopeSystem).filter(TelescopeSystem.id == id).delete()
            self.session.commit()
        except Exception as e:
            print(f"Error occurred while deleting data from the database: {e}")

    def get_all_telescope_systems(self) -> list[TelescopeSystem]:
        """
        Gets all Telescope Systems from the database.

        Returns:
        list[TelescopeSystem] - list of Telescope Systems from the database
        """
        try:
            return self.session.query(TelescopeSystem).all()
        except Exception as e:
            print(f"Error occurred while getting data from the database: {e}")
            return [TelescopeSystem()]

    def update_telescope_system(self, data: TelescopeSystem) -> None:
        """
        Updates data in the database.

        Args:
        data: TelescopeSystem
        """
        try:
            self.session.query(TelescopeSystem).filter(TelescopeSystem.id == data.id).update(data)
            self.session.commit()
        except Exception as e:
            print(f"Error occurred while updating data in the database: {e}")






