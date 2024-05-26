from pydantic import BaseModel


class GroundPointsDto(BaseModel):
    id: int
    NKPOR_Roshydromet: str
    northern_latitude: str
    eastern_longitude: str
    Location: str
    PKI: str
    PKI_developer: str
    types_KA: str
    Reception_speed: str
    radio_channels: int
    modulation_type: str
    polarization_type: str
    reflector_diameter: str
    EIIM_dB_W: str
    Q_factor_dB_K: int
    antenna_gain_coefficient_dB: int
    Receiver_noise_temperature_K: int
    Radio_engineering_system: str
    Kinematic_system: str
    Operating_mode: str
    Maintenance_error: str
    RPU: str
    Antenna_pointing_speed_deg_s: int
    Information_registration_mode: str
    Range_guidance_angles_deg: str
    APS: str
