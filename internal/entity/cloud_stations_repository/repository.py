from internal.usecase.utils import get_session

from sqlalchemy.orm import Session
from internal.entity.cloud_stations_repository.model import CloudStation


class CloudStationRepository(object):
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

    def add_cloud_station(self, data: CloudStation) -> None:
        """
        Adds data to the database.
        Converts dictionary to CloudStation instance and adds it to the database.

        Args:
        data: CloudStation
        """
        try:
            self.session.add(data)
            self.session.commit()
        except Exception as e:
            print(f"Error occurred while adding data to the database: {e}")

    def get_cloud_station_by_id(self, id: int) -> CloudStation:
        """
        Gets data from the database by id.

        Args:
        id: int - id of the data

        Returns:
        CloudStation - data from the database
        """
        try:
            return self.session.query(CloudStation).filter(CloudStation.id == id).first()
        except Exception as e:
            print(f"Error occurred while getting data from the database: {e}")
            return CloudStation()

    def delete_cloud_station_by_id(self, id: int) -> None:
        """
        Deletes data from the database by id.

        Args:
        id: int - id of the data
        """
        try:
            self.session.query(CloudStation).filter(CloudStation.id == id).delete()
            self.session.commit()
        except Exception as e:
            print(f"Error occurred while deleting data from the database: {e}")

    def get_all_cloud_stations(self) -> list[CloudStation]:
        """
        Gets all Cloud Stations from the database.

        Returns:
        list[CloudStation] - list of Cloud Stations from the database
        """
        try:
            return self.session.query(CloudStation).all()
        except Exception as e:
            print(f"Error occurred while getting data from the database: {e}")
            return [CloudStation()]

    def update_cloud_station(self, data: CloudStation) -> None:
        """
        Updates data in the database by id.

        Args:
        data: CloudStation - data to update
        """
        try:
            self.session.query(CloudStation).filter(CloudStation.id == data.id).update(data)
            self.session.commit()
        except Exception as e:
            print(f"Error occurred while updating data in the database: {e}")
