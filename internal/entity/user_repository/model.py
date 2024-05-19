from internal.entity.user_repository.s_constant import USERS_TABLE
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table, ForeignKey, Boolean
from sqlalchemy.orm import registry, declarative_base, Session

Base = declarative_base()
metadata = MetaData()


class User(Base):
    """
    Class for users.
    Contains all the possible fields for the users.
    """
    __tablename__ = USERS_TABLE

    id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=False)
    hashed_password = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    disable = Column(Boolean, default=False)
