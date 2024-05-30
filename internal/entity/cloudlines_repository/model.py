from sqlalchemy import create_engine, Column, Integer, String, MetaData
from sqlalchemy.orm import registry, declarative_base

Base = declarative_base()
metadata = MetaData()

CLOUDLINES = 'cloudlines'


# CREATE table cloudlines (
#     id serial primary key,
#     synoptic_index_of_the_station integer not null default 0,
#     year integer not null default 0,
#     type_of_cloudiness integer not null default 0,
#     average_cloudiness_in_january varchar(40) not null default '',
#     average_cloudiness_in_february varchar(40) not null default '',
#     average_cloudiness_in_march varchar(40) not null default '',
#     average_cloudiness_in_april varchar(40) not null default '',
#     average_cloudiness_in_may varchar(40) not null default '',
#     average_cloudiness_in_june varchar(40) not null default '',
#     average_cloudiness_in_july varchar(40) not null default '',
#     average_cloudiness_in_august varchar(40) not null default '',
#     average_cloudiness_in_september varchar(40) not null default '',
#     average_cloudiness_in_october varchar(40) not null default '',
#     average_cloudiness_in_november varchar(40) not null default '',
#     average_cloudiness_in_december varchar(40) not null default ''
# );


class Cloudlines(Base):
    """
    Class for Cloudlines data.
    Contains all the possible fields for the Cloudlines data.
    """
    __tablename__ = CLOUDLINES

    id = Column(Integer, primary_key=True)
    synoptic_index_of_the_station = Column(Integer, nullable=False, default=0)
    year = Column(Integer, nullable=False, default=0)
    type_of_cloudiness = Column(Integer, nullable=False, default=0)
    average_cloudiness_in_january = Column(String(40), default='')
    average_cloudiness_in_february = Column(String(40), default='')
    average_cloudiness_in_march = Column(String(40), default='')
    average_cloudiness_in_april = Column(String(40), default='')
    average_cloudiness_in_may = Column(String(40), default='')
    average_cloudiness_in_june = Column(String(40), default='')
    average_cloudiness_in_july = Column(String(40), default='')
    average_cloudiness_in_august = Column(String(40), default='')
    average_cloudiness_in_september = Column(String(40), default='')
    average_cloudiness_in_october = Column(String(40), default='')
    average_cloudiness_in_november = Column(String(40), default='')
    average_cloudiness_in_december = Column(String(40), default='')

    def to_dict(self):
        return {
            'synoptic_index_of_the_station': self.synoptic_index_of_the_station,
            'year': self.year,
            'type_of_cloudiness': self.type_of_cloudiness,
            'average_cloudiness_in_january': self.average_cloudiness_in_january,
            'average_cloudiness_in_february': self.average_cloudiness_in_february,
            'average_cloudiness_in_march': self.average_cloudiness_in_march,
            'average_cloudiness_in_april': self.average_cloudiness_in_april,
            'average_cloudiness_in_may': self.average_cloudiness_in_may,
            'average_cloudiness_in_june': self.average_cloudiness_in_june,
            'average_cloudiness_in_july': self.average_cloudiness_in_july,
            'average_cloudiness_in_august': self.average_cloudiness_in_august,
            'average_cloudiness_in_september': self.average_cloudiness_in_september,
            'average_cloudiness_in_october': self.average_cloudiness_in_october,
            'average_cloudiness_in_november': self.average_cloudiness_in_november,
            'average_cloudiness_in_december': self.average_cloudiness_in_december,
        }