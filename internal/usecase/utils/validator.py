import internal.usecase.parser.s_constant
import uuid
from internal.dto import GetShortPathRequest


def validate_dtype(d_type: int) -> bool:
    """
    Validates the data type.
    Checks if the data type is valid.

    Args:
    d_type: int - data type
    """
    match d_type:
        case internal.usecase.parser.s_constant.D_TYPE_EOP:
            return True
        case internal.usecase.parser.s_constant.D_TYPE_SPACE_ENV:
            return True
        case internal.usecase.parser.s_constant.D_TYPE_C20:
            return True
        case _:
            return False


def generate_uuid():
    """
    Generates a UUID.
    """
    return str(uuid.uuid4())



def validate_size(req: GetShortPathRequest) -> bool:
    """
    Validates the size of the matrix.
    Checks if the size of the matrix is valid.

    Args:
    req: GetShortPathRequest - request object
    """
    return req.size * 2 == len(req.flatten_matrix)


