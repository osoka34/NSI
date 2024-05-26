from internal.dto.model_ground_points import GroundPointsDto
from internal.entity.ground_points_repository import GroundPoints


def ground_p_from_repo_to_dto(ground_points: GroundPoints) -> GroundPointsDto:
    ground_points_dto = GroundPointsDto(
        id=ground_points.id,
        NKPOR_Roshydromet=ground_points.NKPOR_Roshydromet,
        northern_latitude=ground_points.northern_latitude,
        eastern_longitude=ground_points.eastern_longitude,
        Location=ground_points.Location,
        PKI=ground_points.PKI,
        PKI_developer=ground_points.PKI_developer,
        types_KA=ground_points.types_KA,
        Reception_speed=ground_points.Reception_speed,
        radio_channels=ground_points.radio_channels,
        modulation_type=ground_points.modulation_type,
        polarization_type=ground_points.polarization_type,
        reflector_diameter=ground_points.reflector_diameter,
        EIIM_dB_W=ground_points.EIIM_dB_W,
        Q_factor_dB_K=ground_points.Q_factor_dB_K,
        antenna_gain_coefficient_dB=ground_points.antenna_gain_coefficient_dB,
        Receiver_noise_temperature_K=ground_points.Receiver_noise_temperature_K,
        Radio_engineering_system=ground_points.Radio_engineering_system,
        Kinematic_system=ground_points.Kinematic_system,
        Operating_mode=ground_points.Operating_mode,
        Maintenance_error=ground_points.Maintenance_error,
        RPU=ground_points.RPU,
        Antenna_pointing_speed_deg_s=ground_points.Antenna_pointing_speed_deg_s,
        Information_registration_mode=ground_points.Information_registration_mode,
        Range_guidance_angles_deg=ground_points.Range_guidance_angles_deg,
        APS=ground_points.APS,
    )

    return ground_points_dto


def ground_p_from_repo_to_dto_list(ground_points: list[GroundPoints]) -> list[GroundPointsDto]:
    gp_list = []
    for gp in ground_points:
        ground_points_dto = GroundPointsDto(
            id=gp.id,
            NKPOR_Roshydromet=gp.NKPOR_Roshydromet,
            northern_latitude=gp.northern_latitude,
            eastern_longitude=gp.eastern_longitude,
            Location=gp.Location,
            PKI=gp.PKI,
            PKI_developer=gp.PKI_developer,
            types_KA=gp.types_KA,
            Reception_speed=gp.Reception_speed,
            radio_channels=gp.radio_channels,
            modulation_type=gp.modulation_type,
            polarization_type=gp.polarization_type,
            reflector_diameter=gp.reflector_diameter,
            EIIM_dB_W=gp.EIIM_dB_W,
            Q_factor_dB_K=gp.Q_factor_dB_K,
            antenna_gain_coefficient_dB=gp.antenna_gain_coefficient_dB,
            Receiver_noise_temperature_K=gp.Receiver_noise_temperature_K,
            Radio_engineering_system=gp.Radio_engineering_system,
            Kinematic_system=gp.Kinematic_system,
            Operating_mode=gp.Operating_mode,
            Maintenance_error=gp.Maintenance_error,
            RPU=gp.RPU,
            Antenna_pointing_speed_deg_s=gp.Antenna_pointing_speed_deg_s,
            Information_registration_mode=gp.Information_registration_mode,
            Range_guidance_angles_deg=gp.Range_guidance_angles_deg,
            APS=gp.APS,
        )
        gp_list.append(ground_points_dto)

    return gp_list


def ground_p_from_dto_to_repo(param: GroundPointsDto) -> GroundPoints:
    ground_points = GroundPoints(
        id=param.id,
        NKPOR_Roshydromet=param.NKPOR_Roshydromet,
        northern_latitude=param.northern_latitude,
        eastern_longitude=param.eastern_longitude,
        Location=param.Location,
        PKI=param.PKI,
        PKI_developer=param.PKI_developer,
        types_KA=param.types_KA,
        Reception_speed=param.Reception_speed,
        radio_channels=param.radio_channels,
        modulation_type=param.modulation_type,
        polarization_type=param.polarization_type,
        reflector_diameter=param.reflector_diameter,
        EIIM_dB_W=param.EIIM_dB_W,
        Q_factor_dB_K=param.Q_factor_dB_K,
        antenna_gain_coefficient_dB=param.antenna_gain_coefficient_dB,
        Receiver_noise_temperature_K=param.Receiver_noise_temperature_K,
        Radio_engineering_system=param.Radio_engineering_system,
        Kinematic_system=param.Kinematic_system,
        Operating_mode=param.Operating_mode,
        Maintenance_error=param.Maintenance_error,
        RPU=param.RPU,
        Antenna_pointing_speed_deg_s=param.Antenna_pointing_speed_deg_s,
        Information_registration_mode=param.Information_registration_mode,
        Range_guidance_angles_deg=param.Range_guidance_angles_deg,
        APS=param.APS,
    )

    return ground_points
