from sqlalchemy import create_engine, Column, Integer, String, MetaData
from sqlalchemy.orm import registry, declarative_base
from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, ARRAY

Base = declarative_base()
metadata = MetaData()

TELESCOPE_SYSTEM_TABLE = 'telescope_system'

class TelescopeSystem(Base):
    """
    Class for Telescope System data.
    Contains all the possible fields for the Telescope System data.
    """
    __tablename__ = TELESCOPE_SYSTEM_TABLE

    id = Column(Integer, primary_key=True)
    telescope = Column(String(50))
    aperture_params = Column(String(50))
    diameter = Column(Float)
    effective_radiation_waist_factor = Column(Float)
    magnification_system = Column(String(50))
    magnification = Column(Float)
    inversion = Column(Boolean)
    gimbal = Column(String(50))
    system_state = Column(String(50))
    x_vector = Column(ARRAY(Float))
    target_internal_state = Column(ARRAY(Float))
    sigma_state_noise = Column(Float)
    constant_system_params = Column(String(50))
    J1 = Column(Float)
    J2 = Column(Float)
    J3 = Column(Float)
    J4 = Column(Float)
    Kg = Column(Float)
    Fs = Column(Float)
    pid_coefs1 = Column(ARRAY(Float))
    pid_coefs2 = Column(ARRAY(Float))
    control_vector = Column(ARRAY(Float))
    real_fsm = Column(String(50))
    state_fsm = Column(String(50))
    x_vector_fsm = Column(ARRAY(Float))
    target_internal_state_fsm = Column(ARRAY(Float))
    sigma_fsm = Column(Float)
    state_limits = Column(ARRAY(Float))
    params_fsm = Column(String(50))
    control_vector_fsm = Column(ARRAY(Float))
    omega01 = Column(ARRAY(Float))
    Q1 = Column(ARRAY(Float))
    Q2 = Column(ARRAY(Float))
    pid_coefs1_fsm = Column(ARRAY(Float))
    pid_coefs2_fsm = Column(ARRAY(Float))
    linear_angle_detector = Column(String(50))
    ideal_lens = Column(String(50))
    distance_to_photodetector = Column(Float)
    matrix_photodetector = Column(String(50))
    pixel_size = Column(ARRAY(Float))
    resolution = Column(ARRAY(Float))
    responsivity = Column(Float)
    uniform_spot = Column(String(50))
    radius = Column(Float)