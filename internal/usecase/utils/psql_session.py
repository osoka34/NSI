import os

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from config import CONFIG as CFG

db_url = (f"postgresql://{CFG['db']['user']}:{CFG['db']['password']}@"
          f"{CFG['db']['host']}:{CFG['db']['port']}/{CFG['db']['database']}")

test_db_url = (f"postgresql://{CFG['test_db']['user']}:{CFG['test_db']['password']}@"
               f"{CFG['test_db']['host']}:{CFG['test_db']['port']}/{CFG['test_db']['database']}")

isTest = os.getenv('TEST', False)


def get_session() -> Session:
    """
    Returns a session to the database.

    Args:
    db_url: str - database URL

    Returns:
    Session - session to the database
    """
    if isTest:
        engine = create_engine(test_db_url)
    else:
        engine = create_engine(db_url)
    _session = sessionmaker(bind=engine)
    session = _session()
    return session
