from internal.usecase.utils import get_session

from sqlalchemy.orm import Session
from internal.entity.project.model import Project


class ProjectRepository(object):
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

    def add_project(self, data: Project) -> None:
        """
        Adds data to the database.
        Converts dictionary to Project instance and adds it to the database.

        Args:
        data: Project
        """
        try:
            self.session.add(data)
            self.session.commit()
        except Exception as e:
            print(f"Error occurred while adding data to the database: {e}")

    def get_project_by_id(self, id: int) -> Project:
        """
        Gets data from the database by id.

        Args:
        id: int - id of the data

        Returns:
        Project - data from the database
        """
        try:
            return self.session.query(Project).filter(Project.id == id).first()
        except Exception as e:
            print(f"Error occurred while getting data from the database: {e}")

    def get_all_projects(self) -> list:
        """
        Gets all data from the database.

        Returns:
        list - all data from the database
        """
        try:
            return self.session.query(Project).all()
        except Exception as e:
            print(f"Error occurred while getting data from the database: {e}")

    def update_project(self, data: Project) -> None:
        """
        Updates data in the database.

        Args:
        data: Project
        """
        try:
            self.session.commit()
        except Exception as e:
            print(f"Error occurred while updating data in the database: {e}")

    def delete_project_by_id(self, in_id: int) -> None:
        """
        Deletes data from the database by id.

        Args:
        id: int - id of the data
        """
        try:
            self.session.query(Project).filter(Project.id == in_id).delete()
            self.session.commit()
        except Exception as e:
            print(f"Error occurred while deleting data from the database: {e}")


