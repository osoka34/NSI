from sqlalchemy import create_engine, Column, Integer, String, MetaData
from sqlalchemy.orm import registry, declarative_base


Base = declarative_base()
metadata = MetaData()

PROJECT = 'project_table'

class Project(Base):
    """
    Class for Project data.
    """
    __tablename__ = PROJECT

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, default='')
    description = Column(String(255), nullable=False, default='')
    created_at = Column(Integer, nullable=False, default=0)

    def to_dict(self):
        """
        Converts the attributes of the NamesConstants instance into a dictionary.
        """
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'created_at': self.created_at
        }