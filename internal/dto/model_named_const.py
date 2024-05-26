from pydantic import BaseModel


class NamedConstantsDto(BaseModel):
    id: int
    const_value: str
    description: str
    const_type: str
    name: str
    dimension: str
