from internal.usecase.utils import get_session

from sqlalchemy.orm import Session
from internal.entity.ground_points_repository.model import GroundPoints


class GroundPointsRepository(object):
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

    def add_ground_points(self, data: GroundPoints) -> None:
        """
        Adds data to the database.
        Converts dictionary to GroundPoints instance and adds it to the database.

        Args:
        data: GroundPoints
        """
        try:
            self.session.add(data)
            self.session.commit()
        except Exception as e:
            print(f"Error occurred while adding data to the database: {e}")

    def get_ground_points_by_id(self, id: int) -> GroundPoints:
        """
        Gets data from the database by id.

        Args:
        id: int - id of the data

        Returns:
        GroundPoints - data from the database
        """
        try:
            return self.session.query(GroundPoints).filter(GroundPoints.id == id).first()
        except Exception as e:
            print(f"Error occurred while getting data from the database: {e}")

    def get_all_ground_points(self) -> list[GroundPoints]:
        """
        Gets all data from the database.

        Returns:
        list[GroundPoints] - all data from the database
        """
        try:
            return self.session.query(GroundPoints).all()
        except Exception as e:
            print(f"Error occurred while getting data from the database: {e}")
            return []

    def delete_ground_points_by_id(self, id: int) -> None:
        """
        Deletes data from the database by id.

        Args:
        id: int - id of the data
        """
        try:
            self.session.query(GroundPoints).filter(GroundPoints.id == id).delete()
            self.session.commit()
        except Exception as e:
            print(f"Error occurred while deleting data from the database: {e}")

    def update_ground_points(self, data: GroundPoints) -> None:
        """
        Updates data in the database.

        Args:
        data: GroundPoints
        """
        try:
            self.session.query(GroundPoints).filter(GroundPoints.id == data.id).update(data.to_dict())
            self.session.commit()
        except Exception as e:
            print(f"Error occurred while updating data in the database: {e}")
