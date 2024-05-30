from pydantic import BaseModel


class TelescopeSystemDto(BaseModel):
    id: int
    telescope: str
    aperture_params: str
    diameter: float
    effective_radiation_waist_factor: float
    magnification_system: str
    magnification: float
    inversion: bool
    gimbal: str
    system_state: str
    x_vector: list
    target_internal_state: list
    sigma_state_noise: float
    constant_system_params: str
    j1_param: float
    j2_param: float
    j3_param: float
    j4_param: float
    kg: float
    fs: float
    pid_coefs1: list
    pid_coefs2: list
    control_vector: list
    real_fsm: str
    state_fsm: str
    x_vector_fsm: list
    target_internal_state_fsm: list
    sigma_fsm: float
    state_limits: list
    params_fsm: str
    control_vector_fsm: list
    omega01: list
    q1_param: list
    q2_param: list
    pid_coefs1_fsm: list
    pid_coefs2_fsm: list
    linear_angle_detector: str
    ideal_lens: str
    distance_to_photodetector: float
    matrix_photodetector: str
    pixel_size: list
    resolution: list
    responsivity: float
    uniform_spot: str
    radius: float


