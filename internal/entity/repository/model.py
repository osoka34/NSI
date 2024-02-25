from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table, ForeignKey, Boolean
from sqlalchemy.orm import registry, declarative_base, Session
from repository.s_constant import NSI_TABLE, LOG_TABLE

Base = declarative_base()
metadata = MetaData()


class NSIData(Base):
    """
    Class for NSI data.
    Contains all the possible fields for the NSI data.
    There are 3 types of data:
    - EOP
    - Space Environment
    - C20
    """
    __tablename__ = NSI_TABLE

    id = Column(Integer, primary_key=True)
    # d_type = Column(Integer, ForeignKey('data_type.id'), nullable=False)
    d_type = Column(Integer)
    year = Column(String(100), default='')
    month = Column(String(100), default='')
    day = Column(String(100), default='')
    mjd = Column(String(100), default='')
    x = Column(String(100), default='')
    y = Column(String(100), default='')
    ut1_utc = Column(String(100), default='')
    lod = Column(String(100), default='')
    dx = Column(String(100), default='')
    dy = Column(String(100), default='')
    x_err = Column(String(100), default='')
    y_err = Column(String(100), default='')
    ut1_utc_err = Column(String(100), default='')
    lod_err = Column(String(100), default='')
    dx_err = Column(String(100), default='')
    dy_err = Column(String(100), default='')
    yyyy = Column(String(100), default='')
    ddd = Column(String(100), default='')
    julianday = Column(String(100), default='')
    f10 = Column(String(100), default='')
    f81c = Column(String(100), default='')
    s10 = Column(String(100), default='')
    s81c = Column(String(100), default='')
    m10 = Column(String(100), default='')
    m81c = Column(String(100), default='')
    y10 = Column(String(100), default='')
    y81c = Column(String(100), default='')
    ssrc = Column(String(100), default='')
    year_c20 = Column(String(100), default='')
    c20 = Column(String(100), default='')
    delta_c20 = Column(String(100), default='')
    c20_sigma = Column(String(100), default='')
    delta_j2 = Column(String(100), default='')
    j2_sigma = Column(String(100), default='')


class RequestLogs(Base):
    """
    Class for request logs.
    Contains all the possible fields for the request logs.
    """
    __tablename__ = LOG_TABLE

    id = Column(Integer, primary_key=True)
    request_time = Column(Integer, default=0)
    request_type = Column(String(100), default='')
    request_data = Column(String(100), default='')
    request_result = Column(Boolean, default=False)
    request_duration = Column(Integer, default=0)
    request_ip = Column(String(100), default='')
    request_user_agent = Column(String(255), default='')
    request_host = Column(String(100), default='')
    request_path = Column(String(100), default='')
    request_query = Column(String(100), default='')
    request_body = Column(String(255), default='')
