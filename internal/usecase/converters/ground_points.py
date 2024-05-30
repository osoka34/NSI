from internal.dto.model_ground_points import GroundPointsDto
from internal.entity.ground_points_repository import GroundPoints


def ground_p_from_repo_to_dto(ground_points: GroundPoints) -> GroundPointsDto:
    ground_points_dto = GroundPointsDto(
        id=ground_points.id,
        nkpor_roshydromet=ground_points.nkpor_roshydromet,
        northern_latitude=ground_points.northern_latitude,
        eastern_longitude=ground_points.eastern_longitude,
        location_param=ground_points.location_param,
        pki=ground_points.pki,
        pki_developer=ground_points.pki_developer,
        types_ka=ground_points.types_ka,
        reception_speed=ground_points.reception_speed,
        radio_channels=ground_points.radio_channels,
        modulation_type=ground_points.modulation_type,
        polarization_type=ground_points.polarization_type,
        reflector_diameter=ground_points.reflector_diameter,
        eiim_db_w=ground_points.eiim_db_w,
        q_factor_d_k=ground_points.q_factor_d_k,
        antenna_gain_coefficient_db=ground_points.antenna_gain_coefficient_db,
        receiver_noise_temperature_k=ground_points.receiver_noise_temperature_k,
        radio_engineering_system=ground_points.radio_engineering_system,
        kinematic_system=ground_points.kinematic_system,
        operating_mode=ground_points.operating_mode,
        maintenance_error=ground_points.maintenance_error,
        rpu=ground_points.rpu,
        antenna_pointing_speed_deg_s=ground_points.antenna_pointing_speed_deg_s,
        information_registration_mode=ground_points.information_registration_mode,
        range_guidance_angles_deg=ground_points.range_guidance_angles_deg,
        aps=ground_points.aps,
    )

    return ground_points_dto


def ground_p_from_repo_to_dto_list(ground_points: list[GroundPoints]) -> list[GroundPointsDto]:
    gp_list = []
    for gp in ground_points:
        ground_points_dto = GroundPointsDto(
            id=gp.id,
            nkpor_roshydromet=gp.nkpor_roshydromet,
            northern_latitude=gp.northern_latitude,
            eastern_longitude=gp.eastern_longitude,
            location_param=gp.location_param,
            pki=gp.pki,
            pki_developer=gp.pki_developer,
            types_ka=gp.types_ka,
            reception_speed=gp.reception_speed,
            radio_channels=gp.radio_channels,
            modulation_type=gp.modulation_type,
            polarization_type=gp.polarization_type,
            reflector_diameter=gp.reflector_diameter,
            eiim_db_w=gp.eiim_db_w,
            q_factor_d_k=gp.q_factor_d_k,
            antenna_gain_coefficient_db=gp.antenna_gain_coefficient_db,
            receiver_noise_temperature_k=gp.receiver_noise_temperature_k,
            radio_engineering_system=gp.radio_engineering_system,
            kinematic_system=gp.kinematic_system,
            operating_mode=gp.operating_mode,
            maintenance_error=gp.maintenance_error,
            rpu=gp.rpu,
            antenna_pointing_speed_deg_s=gp.antenna_pointing_speed_deg_s,
            information_registration_mode=gp.information_registration_mode,
            range_guidance_angles_deg=gp.range_guidance_angles_deg,
            aps=gp.aps,
        )
        gp_list.append(ground_points_dto)

    return gp_list


def ground_p_from_dto_to_repo(param: GroundPointsDto) -> GroundPoints:
    ground_points = GroundPoints(
        id=param.id,
        nkpor_roshydromet=param.nkpor_roshydromet,
        northern_latitude=param.northern_latitude,
        eastern_longitude=param.eastern_longitude,
        location_param=param.location_param,
        pki=param.pki,
        pki_developer=param.pki_developer,
        types_ka=param.types_ka,
        reception_speed=param.reception_speed,
        radio_channels=param.radio_channels,
        modulation_type=param.modulation_type,
        polarization_type=param.polarization_type,
        reflector_diameter=param.reflector_diameter,
        eiim_db_w=param.eiim_db_w,
        q_factor_d_k=param.q_factor_d_k,
        antenna_gain_coefficient_db=param.antenna_gain_coefficient_db,
        receiver_noise_temperature_k=param.receiver_noise_temperature_k,
        radio_engineering_system=param.radio_engineering_system,
        kinematic_system=param.kinematic_system,
        operating_mode=param.operating_mode,
        maintenance_error=param.maintenance_error,
        rpu=param.rpu,
        antenna_pointing_speed_deg_s=param.antenna_pointing_speed_deg_s,
        information_registration_mode=param.information_registration_mode,
        range_guidance_angles_deg=param.range_guidance_angles_deg,
        aps=param.aps,
    )

    return ground_points
