from pydantic import BaseModel


class GroundPointsDto(BaseModel):
    id: int
    nkpor_roshydromet: str
    northern_latitude: str
    eastern_longitude: str
    location_param: str
    pki: str
    pki_developer: str
    types_ka: str
    reception_speed: str
    radio_channels: int
    modulation_type: str
    polarization_type: str
    reflector_diameter: str
    eiim_db_w: str
    q_factor_d_k: int
    antenna_gain_coefficient_db: int
    receiver_noise_temperature_k: int
    radio_engineering_system: str
    kinematic_system: str
    operating_mode: str
    maintenance_error: str
    rpu: str
    antenna_pointing_speed_deg_s: int
    information_registration_mode: str
    range_guidance_angles_deg: str
    aps: str
