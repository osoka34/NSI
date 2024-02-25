from internal.usecase.utils import get_session
from fastapi import Depends

from internal.entity.repository.model import NSIData, RequestLogs
from sqlalchemy.orm import Session


class Repository(object):
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
        We use Depends to get the session from the get_session function.

        """
        self.session = session

    # def __del__(self):
    #     """
    #     Destructor for Repository class.
    #     Closes the connection to the database.
    #     """
    #     if self.session:
    #         self.session.close()

    def close(self):
        """
        Closes the connection to the database.
        """

        if self.session:
            self.session.close()
            self.session = None

    def add_nsi_data_list(self, data: list[dict]) -> None:
        """
        Adds data to the database.
        Converts list of dictionaries to list of NSIData instances and adds them to the database.

        Args:
        data: list[dict] - list of dictionaries with data

        """
        try:
            instances = [NSIData(**d) for d in data]
            self.session.add_all(instances)
            self.session.commit()
        except Exception as e:
            print(f"Error occurred while adding data to the database: {e}")

    def add_nsi_data_one(self, data: dict) -> None:
        """
        Adds data to the database.
        Converts dictionary to NSIData instance and adds it to the database.

        Args:
        data: dict - dictionary with data

        """
        try:
            instance = NSIData(**data)
            self.session.add(instance)
            self.session.commit()
        except Exception as e:
            print(f"Error occurred while adding data to the database: {e}")

    def add_request_logs(self, data: RequestLogs) -> None:
        """
        Adds request logs to the database.

        Args:
        data: RequestLogs - request logs instance

        """
        try:
            self.session.add(data)
            self.session.commit()
        except Exception as e:
            print(f"Error occurred while adding data to the database: {e}")

    def get_nsi_data(self) -> list:
        """
        Gets all NSI data from the database.

        Returns:
        list[NSIData] - list of NSIData instances

        """
        try:
            return self.session.query(NSIData).all()
        except Exception as e:
            print(f"Error occurred while getting data from the database: {e}")
            return []

    def get_nsi_data_view(self, d_type: int, limit: int = 10) -> list[NSIData]:
        """
        Gets NSI data from the database by type.
        Uses limit to get a limited amount of data.
        If limit set to 0, gets all data of the specified type.

        Args:
        d_type: int - data type
        limit: int - limit of data, default 10

        Returns:
        list[NSIData] - list of NSIData instances
        """
        if limit:
            try:
                return self.session.query(NSIData).filter(NSIData.d_type == d_type).limit(limit).all()
            except Exception as e:
                print(f"Error occurred while getting data from the database: {e}")
                return []
        else:
            try:
                return self.session.query(NSIData).filter(NSIData.d_type == d_type).all()
            except Exception as e:
                print(f"Error occurred while getting data from the database: {e}")
                return []
