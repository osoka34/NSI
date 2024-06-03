from internal.dto.model_nsi import LoadNSIRequest, DefaultResponse, GetNSIRequest, GetNSIResponse, NSI_BAD_REQUEST
from internal.dto.model_graph import GetShortPathRequest, GRAPH_BAD_REQUEST
from internal.dto.model_auth import Token, TokenData, UserDto
from pydantic import BaseModel
from internal.dto.model_named_const import NamedConstantsDto
from internal.dto.model_cloud_stations import CloudStationDto
from internal.dto.model_telescope_system import TelescopeSystemDto
from internal.dto.model_named_const import NamedConstantsDto
from internal.dto.model_ground_points import GroundPointsDto
from internal.dto.model_cloudlines import CloudlinesDto
from internal.dto.model_platform_ca import PlatformCADto
from internal.dto.model_project import ProjectDto



class ById (BaseModel):
    id: int
