from internal.entity.repository.repository import Repository
from internal.entity.repository.model import NSIData, RequestLogs


def get_repository() -> Repository:
    """
    Fabric method for Repository class.
    """
    repo = Repository()
    return repo


