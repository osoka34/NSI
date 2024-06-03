from pydantic import BaseModel


class ProjectDto(BaseModel):
    id: int
    name: str
    description: str
    created_at: int
