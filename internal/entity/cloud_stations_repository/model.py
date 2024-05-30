from sqlalchemy import create_engine, Column, Integer, String, MetaData
from sqlalchemy.orm import registry, declarative_base

Base = declarative_base()
metadata = MetaData()

CLOUD_STATIONS = 'cloud_stations'



class CloudStation(Base):
    """
    Class for Cloud Station data.
    Contains all the possible fields for the Cloud Station data.
    """
    __tablename__ = CLOUD_STATIONS

    id = Column(Integer, primary_key=True)
    index_vmo = Column(Integer, nullable=False)
    station_name = Column(String(255), default='')
    latitude = Column(String(20), default='')
    longitude = Column(String(20), default='')
    height_homeopost = Column(Integer, default=0)
    collect_from = Column(Integer, default=0)
    note = Column(String(255), default='')

    def to_dict(self):
        """
        Converts the attributes of the CloudStation instance into a dictionary.
        """
        return {
            'id': self.id,
            'index_vmo': self.index_vmo,
            'station_name': self.station_name,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'height_homeopost': self.height_homeopost,
            'collect_from': self.collect_from,
            'note': self.note
        }




