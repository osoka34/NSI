from sqlalchemy import create_engine, Column, Integer, String, MetaData
from sqlalchemy.orm import registry, declarative_base


Base = declarative_base()
metadata = MetaData()

NAMED_CONSTANTS = 'named_constants'


class NamesConstants(Base):
    """
    Class for Ground Points data.
    Contains all the possible fields for the Ground Points data.
    """
    __tablename__ = NAMED_CONSTANTS

    id = Column(Integer, primary_key=True)
    const_value = Column(String(255), nullable=False, default='')
    description = Column(String(255), nullable=False, default='')
    const_type = Column(String(255), nullable=False, default='')
    name = Column(String(255), nullable=False, default='')
    dimension = Column(String(255), nullable=False, default='')

    def to_dict(self):
        """
        Converts the attributes of the NamesConstants instance into a dictionary.
        """
        return {
            'id': self.id,
            'const_value': self.const_value,
            'description': self.description,
            'const_type': self.const_type,
            'name': self.name,
            'dimension': self.dimension
        }

# from internal.dto import NamedConstantsDto
# nc = NamedConstantsDto(id=1, const_value="const_value", description="description", const_type="const_type", name="name", dimension="dimension")
#
#
# nc_repo = NamesConstants(id=nc.id, const_value=nc.const_value, description=nc.description, const_type=nc.const_type, name=nc.name, dimension=nc.dimension)
# print(nc_repo)





