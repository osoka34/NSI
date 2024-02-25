import internal.usecase.parser.s_constant
import uuid


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
    return str(uuid.uuid4())


