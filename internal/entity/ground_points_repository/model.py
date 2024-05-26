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
    NKPOR_Roshydromet = Column(String(255), nullable=False, default='')
    northern_latitude = Column(String(255), nullable=False, default='')
    eastern_longitude = Column(String(255), nullable=False, default='')
    Location = Column(String(255), nullable=False, default='')
    PKI = Column(String(255), nullable=False, default='')
    PKI_developer = Column(String(255), nullable=False, default='')
    types_KA = Column(String(255), nullable=False, default='')
    Reception_speed = Column(String(255), nullable=False, default='')
    radio_channels = Column(Integer, nullable=False, default=0)
    modulation_type = Column(String(255), nullable=False, default='')
    polarization_type = Column(String(255), nullable=False, default='')
    reflector_diameter = Column(String(255), nullable=False, default='')
    EIIM_dB_W = Column(String(255), nullable=False, default='')
    Q_factor_dB_K = Column(Integer, nullable=False, default=0)
    antenna_gain_coefficient_dB = Column(Integer, nullable=False, default=0)
    Receiver_noise_temperature_K = Column(Integer, nullable=False, default=0)
    Radio_engineering_system = Column(String(255), nullable=False, default='')
    Kinematic_system = Column(String(255), nullable=False, default='')
    Operating_mode = Column(String(255), nullable=False, default='')
    Maintenance_error = Column(String(255), nullable=False, default='')
    RPU = Column(String(255), nullable=False, default='')
    Antenna_pointing_speed_deg_s = Column(Integer, nullable=False, default=0)
    Information_registration_mode = Column(String(255), nullable=False, default='')
    Range_guidance_angles_deg = Column(String(255), nullable=False, default='')
    APS = Column(String(255), nullable=False, default='')
