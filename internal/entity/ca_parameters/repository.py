from internal.usecase.utils import get_session
from sqlalchemy.orm import Session
from sqlalchemy import text
from internal.entity.ca_parameters.model import CAParameters, CAPlatformView


class CAParametersRepository(object):
    """
    Class for working with the database.

    Attributes:
    session: Session - connection to the database
    """

    def __init__(self, session: Session = get_session()):
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

    def add_ca_parameters(self, data: CAParameters) -> None:
        """
        Adds data to the database.
        Converts dictionary to CAParameters instance and adds it to the database.

        Args:
        data: CAParameters
        """
        try:
            self.session.add(data)
            self.session.commit()
        except Exception as e:
            print(f"Error occurred while adding data to the database: {e}")

    def get_ca_parameters_by_id(self, id: int) -> CAParameters:
        """
        Gets data from the database by id.

        Args:
        id: int - id of the data

        Returns:
        CAParameters - data from the database
        """
        try:
            return self.session.query(CAParameters).filter(CAParameters.id == id).first()
        except Exception as e:
            print(f"Error occurred while getting data from the database: {e}")

    def get_all_ca_parameters(self) -> list:
        """
        Gets all data from the database.

        Returns:
        list - all data from the database
        """
        try:
            return self.session.query(CAParameters).all()
        except Exception as e:
            print(f"Error occurred while getting data from the database: {e}")

    def update_ca_parameters(self, id: int, data: CAParameters) -> None:
        """
        Updates data in the database.

        Args:
        id: int - id of the data
        data: CAParameters - new data
        """
        try:
            self.session.query(CAParameters).filter(CAParameters.id == id).update(data.to_dict())
            self.session.commit()
        except Exception as e:
            print(f"Error occurred while updating data in the database: {e}")

    def delete_ca_parameters(self, id: int) -> None:
        """
        Deletes data from the database.

        Args:
        id: int - id of the data
        """
        try:
            self.session.query(CAParameters).filter(CAParameters.id == id).delete()
            self.session.commit()
        except Exception as e:
            print(f"Error occurred while deleting data from the database: {e}")

    def get_all_ca_platform_view(self) -> list:
        """
        Gets data from the view by ca_id.

        Returns:
        list - data from the view
        """
        try:
            query = text("""
                                SELECT
                                    *
                                FROM
                                    ca_platform_view
                            """)
            result = self.session.execute(query).fetchall()
            return result
        except Exception as e:
            print(f"Error occurred while getting data from the view: {e}")

    def get_all_by_id_ca_platform_view(self, ca_id: int) -> list:
        """
         results = self.session.query(CAPlatformView).
            filter(CAPlatformView.ca_id == ca_id).
                all() -- не работает почему-то, возвращает только по одной записи на каждый ca_id

        обычно * использовать плохо, но в данном случае это не так, так как вьюшка не будет меняться
        и не будет добавляться новых полей, поэтому можно использовать *

        Gets all data from the view.

        Args:
        ca_id: int - id of the data

        Returns:
        list - all data from the view
        """
        try:
            query = text("""
                    SELECT
                        *
                    FROM
                        ca_platform_view
                    WHERE
                        ca_id = :ca_id
                """)
            result = self.session.execute(query, {"ca_id": ca_id}).fetchall()
            return result
        except Exception as e:
            print(f"Error occurred while getting data from the view: {e}")
