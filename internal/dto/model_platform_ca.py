from pydantic import BaseModel


class PlatformCADto(BaseModel):
    id: int
    structure: str
    weight: float
    power_consumption_in_standby_mode: float
    power_consumption_in_the_high_speed_mode: float
    power_consumption_in_the_orbit_correction_mode: float
    power_consumption_in_safe_mode: float
    power_consumption_in_ca_operational_mode: float
    average_power_consumption_per_cycle: float
    mdr: float
    sac: float
    reliability_budget: float
    type_platform: int

