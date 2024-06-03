from internal.entity.platform_ca import PlatformCA
from internal.dto import PlatformCADto
def platform_ca_from_repo_to_dto(platform_ca: PlatformCA) -> PlatformCADto:
    return PlatformCADto(
        id=platform_ca.id,
        structure=platform_ca.structure,
        weight=platform_ca.weight,
        power_consumption_in_standby_mode=platform_ca.power_consumption_in_standby_mode,
        power_consumption_in_the_high_speed_mode=platform_ca.power_consumption_in_the_high_speed_mode,
        power_consumption_in_the_orbit_correction_mode=platform_ca.power_consumption_in_the_orbit_correction_mode,
        power_consumption_in_safe_mode=platform_ca.power_consumption_in_safe_mode,
        power_consumption_in_ca_operational_mode=platform_ca.power_consumption_in_ca_operational_mode,
        average_power_consumption_per_cycle=platform_ca.average_power_consumption_per_cycle,
        mdr=platform_ca.mdr,
        sac=platform_ca.sac,
        reliability_budget=platform_ca.reliability_budget,
        type_platform=platform_ca.type_platform
    )

def platform_ca_from_repo_to_dto_list(params: list[PlatformCA]) -> list[PlatformCADto]:
    l = []
    for c in params:
        l.append(PlatformCADto(
            id=c.id,
            structure=c.structure,
            weight=c.weight,
            power_consumption_in_standby_mode=c.power_consumption_in_standby_mode,
            power_consumption_in_the_high_speed_mode=c.power_consumption_in_the_high_speed_mode,
            power_consumption_in_the_orbit_correction_mode=c.power_consumption_in_the_orbit_correction_mode,
            power_consumption_in_safe_mode=c.power_consumption_in_safe_mode,
            power_consumption_in_ca_operational_mode=c.power_consumption_in_ca_operational_mode,
            average_power_consumption_per_cycle=c.average_power_consumption_per_cycle,
            mdr=c.mdr,
            sac=c.sac,
            reliability_budget=c.reliability_budget,
            type_platform=c.type_platform
        ))
    return l


def platform_ca_from_dto_to_repo(platform_ca: PlatformCADto) -> PlatformCA:
    return PlatformCA(
        id=platform_ca.id,
        structure=platform_ca.structure,
        weight=platform_ca.weight,
        power_consumption_in_standby_mode=platform_ca.power_consumption_in_standby_mode,
        power_consumption_in_the_high_speed_mode=platform_ca.power_consumption_in_the_high_speed_mode,
        power_consumption_in_the_orbit_correction_mode=platform_ca.power_consumption_in_the_orbit_correction_mode,
        power_consumption_in_safe_mode=platform_ca.power_consumption_in_safe_mode,
        power_consumption_in_ca_operational_mode=platform_ca.power_consumption_in_ca_operational_mode,
        average_power_consumption_per_cycle=platform_ca.average_power_consumption_per_cycle,
        mdr=platform_ca.mdr,
        sac=platform_ca.sac,
        reliability_budget=platform_ca.reliability_budget,
        type_platform=platform_ca.type_platform
    )
