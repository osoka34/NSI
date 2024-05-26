from typing import Any

from starlette.responses import JSONResponse

from internal.entity.named_constants_repository import NamesConstantsRepository
from internal.dto import NamedConstantsDto, ById
from internal.entity.named_constants_repository import NamesConstants
from fastapi import status, HTTPException, Depends


class ApplicationNamedConstService(object):
    def __init__(
            self,
    ):
        self.repository = NamesConstantsRepository()

    def add_named_const(self, named_const: NamedConstantsDto):
        try:
            named_const_repo = NamesConstants(id=named_const.id, const_value=named_const.const_value,
                                              description=named_const.description, const_type=named_const.const_type,
                                              name=named_const.name, dimension=named_const.dimension)
            self.repository.add_named_constants(named_const_repo)
            return JSONResponse(status_code=status.HTTP_200_OK, content=named_const)
        except Exception as e:
            print(f"ERROR ::: ApplicationNamedConst -> add_named_const: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_ERROR,
                detail="Internal server error",
            )

    def get_named_const_by_id(self, in_id: int):
        try:
            named_const = self.repository.get_named_constants_by_id(in_id)
            named_dto = NamedConstantsDto(id=named_const.id, const_value=named_const.const_value,
                                          description=named_const.description, const_type=named_const.const_type,
                                          name=named_const.name, dimension=named_const.dimension)
            if not named_const:
                return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,
                                    content={"success": False, "description": "Named constant not found"})
            return JSONResponse(status_code=status.HTTP_200_OK, content=named_dto)
        except Exception as e:
            print(f"ERROR ::: ApplicationNamedConst -> get_named_const_by_id: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_ERROR,
                detail="Internal server error",
            )

    def get_all_named_const(self):
        try:
            named_const = self.repository.get_all_named_constants()
            if not named_const:
                return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,
                                    content={"success": False, "description": "Named constant not found"})
            return JSONResponse(status_code=status.HTTP_200_OK, content=named_const)
        except Exception as e:
            print(f"ERROR ::: ApplicationNamedConst -> get_all_named_const: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_ERROR,
                detail="Internal server error",
            )

    def update_named_const(self, named_const: NamedConstantsDto):
        try:
            named_const_repo = NamesConstants(id=named_const.id, const_value=named_const.const_value,
                                              description=named_const.description, const_type=named_const.const_type,
                                              name=named_const.name, dimension=named_const.dimension)
            self.repository.update_named_constants(named_const_repo)
            return JSONResponse(status_code=status.HTTP_200_OK, content=named_const)
        except Exception as e:
            print(f"ERROR ::: ApplicationNamedConst -> update_named_const: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_ERROR,
                detail="Internal server error",
            )

    def delete_named_const(self, in_id: int):
        try:
            self.repository.delete_named_constants_by_id(in_id)
            return JSONResponse(status_code=status.HTTP_200_OK,
                                content={"success": True, "description": "Named constant deleted"})
        except Exception as e:
            print(f"ERROR ::: ApplicationNamedConst -> delete_named_const: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_ERROR,
                detail="Internal server error",
            )
