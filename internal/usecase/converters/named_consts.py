from internal.entity.named_constants_repository import NamesConstants
from internal.dto import NamedConstantsDto


def named_const_from_repo_to_dto(named_const: NamesConstants) -> NamedConstantsDto:
    return NamedConstantsDto(
        id=named_const.id,
        const_value=named_const.const_value,
        description=named_const.description,
        const_type=named_const.const_type,
        name=named_const.name,
        dimension=named_const.dimension
    )


def named_const_from_repo_to_dto_list(params: list[NamesConstants]) -> list[NamedConstantsDto]:
    l = []
    for c in params:
        l.append(NamedConstantsDto(
            id=c.id,
            const_value=c.const_value,
            description=c.description,
            const_type=c.const_type,
            name=c.name,
            dimension=c.dimension
        ))
    return l


def named_const_from_dto_to_repo(named_const: NamedConstantsDto) -> NamesConstants:
    return NamesConstants(
        id=named_const.id,
        const_value=named_const.const_value,
        description=named_const.description,
        const_type=named_const.const_type,
        name=named_const.name,
        dimension=named_const.dimension
    )
