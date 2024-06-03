from typing import Any

from starlette.responses import JSONResponse

from internal.entity.project import ProjectRepository, Project
from internal.dto import ProjectDto, ById
from fastapi import status, HTTPException, Depends


class ApplicationProjectService(object):
    def __init__(
            self,
    ):
        self.repository = ProjectRepository()

    def add_project(self, project: ProjectDto) -> JSONResponse:
        try:
            project_repo = Project(id=project.id, name=project.name, description=project.description,
                                   created_at=project.created_at)
            self.repository.add_project(project_repo)
            return JSONResponse(status_code=status.HTTP_200_OK, content={"success": True})
        except Exception as e:
            print(f"ERROR ::: ApplicationProject -> add_project: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Internal server error",
            )

    def get_project_by_id(self, in_id: int) -> JSONResponse | ProjectDto:
        try:
            project = self.repository.get_project_by_id(in_id)
            if not project:
                return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,
                                    content={"success": False, "description": "Project not found"})
            project_dto = ProjectDto(id=project.id, name=project.name, description=project.description,
                                     created_at=project.created_at)
            return project_dto
        except Exception as e:
            print(f"ERROR ::: ApplicationProject -> get_project_by_id: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Internal server error",
            )

    def get_all_project(self) -> JSONResponse | Any:
        try:
            project = self.repository.get_all_projects()
            if not project:
                return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,
                                    content={"success": False, "description": "Project not found"})
            project_dto = []
            for proj in project:
                project_dto.append(ProjectDto(id=proj.id, name=proj.name, description=proj.description,
                                              created_at=proj.created_at))
            return {"data": project_dto}
        except Exception as e:
            print(f"ERROR ::: ApplicationProject -> get_all_project: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def update_project(self, project: ProjectDto) -> JSONResponse:
        try:
            project_repo = Project(id=project.id, name=project.name, description=project.description,
                                   created_at=project.created_at)
            self.repository.update_project(project_repo)
            return JSONResponse(status_code=status.HTTP_200_OK, content={"success": True})
        except Exception as e:
            print(f"ERROR ::: ApplicationProject -> update_project: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Internal server error",
            )

    def delete_project(self, in_id: int) -> JSONResponse:
        try:
            self.repository.delete_project_by_id(in_id)
            return JSONResponse(status_code=status.HTTP_200_OK, content={"success": True})
        except Exception as e:
            print(f"ERROR ::: ApplicationProject -> delete_project: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Internal server error",
            )
