from sqlalchemy import create_engine, Column, Integer, String, MetaData
from sqlalchemy.orm import registry, declarative_base

Base = declarative_base()
metadata = MetaData()

CLOUDLINES = 'cloudlines'


# CREATE table cloudlines (
#     id serial primary key,
#     Synoptic_index_of_thу_station integer not null default 0,
#     Year integer not null default 0,
#     Type_of_cloudiness integer not null default 0,
#     Average_cloudiness_in_January varchar(40) not null default '',
#     Average_cloudiness_in_February varchar(40) not null default '',
#     Average_cloudiness_in_March varchar(40) not null default '',
#     Average_cloudiness_in_April varchar(40) not null default '',
#     Average_cloudiness_in_May varchar(40) not null default '',
#     Average_cloudiness_in_June varchar(40) not null default '',
#     Average_cloudiness_in_July varchar(40) not null default '',
#     Average_cloudiness_in_August varchar(40) not null default '',
#     Average_cloudiness_in_September varchar(40) not null default '',
#     Average_cloudiness_in_October varchar(40) not null default '',
#     Average_cloudiness_in_November varchar(40) not null default '',
#     Average_cloudiness_in_December varchar(40) not null default ''
# );


class Cloudlines(Base):
    """
    Class for Cloudlines data.
    Contains all the possible fields for the Cloudlines data.
    """
    __tablename__ = CLOUDLINES

    id = Column(Integer, primary_key=True)
    Synoptic_index_of_thу_station = Column(Integer, nullable=False, default=0)
    Year = Column(Integer, nullable=False, default=0)
    Type_of_cloudiness = Column(Integer, nullable=False, default=0)
    Average_cloudiness_in_January = Column(String(40), default='')
    Average_cloudiness_in_February = Column(String(40), default='')
    Average_cloudiness_in_March = Column(String(40), default='')
    Average_cloudiness_in_April = Column(String(40), default='')
    Average_cloudiness_in_May = Column(String(40), default='')
    Average_cloudiness_in_June = Column(String(40), default='')
    Average_cloudiness_in_July = Column(String(40), default='')
    Average_cloudiness_in_August = Column(String(40), default='')
    Average_cloudiness_in_September = Column(String(40), default='')
    Average_cloudiness_in_October = Column(String(40), default='')
    Average_cloudiness_in_November = Column(String(40), default='')
    Average_cloudiness_in_December = Column(String(40), default='')