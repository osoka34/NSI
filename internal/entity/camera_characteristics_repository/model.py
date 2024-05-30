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
    j1_param = Column(Float)
    j2_param = Column(Float)
    j3_param = Column(Float)
    j4_param = Column(Float)
    kg = Column(Float)
    fs = Column(Float)
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
    q1_param = Column(ARRAY(Float))
    q2_param = Column(ARRAY(Float))
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

    def to_dict(self):
        """
        Converts the attributes of the TelescopeSystem instance into a dictionary.
        """
        return {
            'telescope': self.telescope,
            'aperture_params': self.aperture_params,
            'diameter': self.diameter,
            'effective_radiation_waist_factor': self.effective_radiation_waist_factor,
            'magnification_system': self.magnification_system,
            'magnification': self.magnification,
            'inversion': self.inversion,
            'gimbal': self.gimbal,
            'system_state': self.system_state,
            'x_vector': self.x_vector,
            'target_internal_state': self.target_internal_state,
            'sigma_state_noise': self.sigma_state_noise,
            'constant_system_params': self.constant_system_params,
            'j1_param': self.j1_param,
            'j2_param': self.j2_param,
            'j3_param': self.j3_param,
            'j4_param': self.j4_param,
            'kg': self.kg,
            'fs': self.fs,
            'pid_coefs1': self.pid_coefs1,
            'pid_coefs2': self.pid_coefs2,
            'control_vector': self.control_vector,
            'real_fsm': self.real_fsm,
            'state_fsm': self.state_fsm,
            'x_vector_fsm': self.x_vector_fsm,
            'target_internal_state_fsm': self.target_internal_state_fsm,
            'sigma_fsm': self.sigma_fsm,
            'state_limits': self.state_limits,
            'params_fsm': self.params_fsm,
            'control_vector_fsm': self.control_vector_fsm,
            'omega01': self.omega01,
            'q1_param': self.q1_param,
            'q2_param': self.q2_param,
            'pid_coefs1_fsm': self.pid_coefs1_fsm,
            'pid_coefs2_fsm': self.pid_coefs2_fsm,
            'linear_angle_detector': self.linear_angle_detector,
            'ideal_lens': self.ideal_lens,
            'distance_to_photodetector': self.distance_to_photodetector,
            'matrix_photodetector': self.matrix_photodetector,
            'pixel_size': self.pixel_size,
            'resolution': self.resolution,
            'responsivity': self.responsivity,
            'uniform_spot': self.uniform_spot,
            'radius': self.radius
        }


