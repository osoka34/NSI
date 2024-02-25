from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from config import CONFIG as CFG

db_url = (f"postgresql://{CFG['db']['user']}:{CFG['db']['password']}@"
          f"{CFG['db']['host']}:{CFG['db']['port']}/{CFG['db']['database']}")


def get_session() -> Session:
    """
    Returns a session to the database.

    Args:
    db_url: str - database URL

    Returns:
    Session - session to the database
    """
    engine = create_engine(db_url)
    _session = sessionmaker(bind=engine)
    session = _session()
    return session
