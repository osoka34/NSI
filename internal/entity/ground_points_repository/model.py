from sqlalchemy import create_engine, Column, Integer, String, MetaData
from sqlalchemy.orm import registry, declarative_base


Base = declarative_base()
metadata = MetaData()

GROUND_POINTS = 'ground_points'

class GroundPoints(Base):
    """
    Class for Ground Points data.
    Contains all the possible fields for the Ground Points data.
    """
    __tablename__ = GROUND_POINTS

    id = Column(Integer, primary_key=True)
    nkpor_roshydromet = Column(String(255), nullable=False, default='')
    northern_latitude = Column(String(255), nullable=False, default='')
    eastern_longitude = Column(String(255), nullable=False, default='')
    location_param = Column(String(255), nullable=False, default='')
    pki = Column(String(255), nullable=False, default='')
    pki_developer = Column(String(255), nullable=False, default='')
    types_ka = Column(String(255), nullable=False, default='')
    reception_speed = Column(String(255), nullable=False, default='')
    radio_channels = Column(Integer, nullable=False, default=0)
    modulation_type = Column(String(255), nullable=False, default='')
    polarization_type = Column(String(255), nullable=False, default='')
    reflector_diameter = Column(String(255), nullable=False, default='')
    eiim_db_w = Column(String(255), nullable=False, default='')
    q_factor_d_k = Column(Integer, nullable=False, default=0)
    antenna_gain_coefficient_db = Column(Integer, nullable=False, default=0)
    receiver_noise_temperature_k = Column(Integer, nullable=False, default=0)
    radio_engineering_system = Column(String(255), nullable=False, default='')
    kinematic_system = Column(String(255), nullable=False, default='')
    operating_mode = Column(String(255), nullable=False, default='')
    maintenance_error = Column(String(255), nullable=False, default='')
    rpu = Column(String(255), nullable=False, default='')
    antenna_pointing_speed_deg_s = Column(Integer, nullable=False, default=0)
    information_registration_mode = Column(String(255), nullable=False, default='')
    range_guidance_angles_deg = Column(String(255), nullable=False, default='')
    aps = Column(String(255), nullable=False, default='')

    def to_dict(self):
        """
        Converts the attributes of the GroundPoints instance into a dictionary.
        """
        return {
            'id': self.id,
            'nkpor_roshydromet': self.nkpor_roshydromet,
            'northern_latitude': self.northern_latitude,
            'eastern_longitude': self.eastern_longitude,
            'location_param': self.location_param,
            'pki': self.pki,
            'pki_developer': self.pki_developer,
            'types_ka': self.types_ka,
            'reception_speed': self.reception_speed,
            'radio_channels': self.radio_channels,
            'modulation_type': self.modulation_type,
            'polarization_type': self.polarization_type,
            'reflector_diameter': self.reflector_diameter,
            'eiim_db_w': self.eiim_db_w,
            'q_factor_d_k': self.q_factor_d_k,
            'antenna_gain_coefficient_db': self.antenna_gain_coefficient_db,
            'receiver_noise_temperature_k': self.receiver_noise_temperature_k,
            'radio_engineering_system': self.radio_engineering_system,
            'kinematic_system': self.kinematic_system,
            'operating_mode': self.operating_mode,
            'maintenance_error': self.maintenance_error,
            'rpu': self.rpu,
            'antenna_pointing_speed_deg_s': self.antenna_pointing_speed_deg_s,
            'information_registration_mode': self.information_registration_mode,
            'range_guidance_angles_deg': self.range_guidance_angles_deg,
            'aps': self.aps
        }

