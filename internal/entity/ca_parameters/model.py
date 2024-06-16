from sqlalchemy import create_engine, Column, Integer, String, Float, MetaData, Table
from sqlalchemy.orm import registry, declarative_base, sessionmaker

Base = declarative_base()
metadata = MetaData()

CA_PLATFORM_VIEW = 'ca_platform_view'
CA_PARAMETERS = 'ca_parameters'


class CAPlatformView(Base):
    """
    Class for CAPlatformView data.
    """
    __tablename__ = CA_PLATFORM_VIEW

    ca_id = Column(Integer, primary_key=True)
    name_of_the_ca = Column(String, nullable=False, default='')
    number_of_spectral_channels_px = Column(Integer, nullable=False, default=0)
    parameters_of_the_panchromatic_channel_nm = Column(String, nullable=False, default='')
    number_of_spectral_channels_ms = Column(Integer, nullable=False, default=0)
    parameters_of_the_red_channel_nm = Column(String, nullable=False, default='')
    parameters_of_the_green_channel_nm = Column(String, nullable=False, default='')
    parameters_of_the_blue_channel_nm = Column(String, nullable=False, default='')
    parameters_of_the_near_infrared_channel_nm = Column(String, nullable=False, default='')
    adc_bit_depth_bits = Column(Integer, nullable=False, default=0)
    bit_depth_of_transmitted_information_bits = Column(Integer, nullable=False, default=0)
    shooting_mode = Column(String, nullable=False, default='')
    interface = Column(String, nullable=False, default='')
    data_stream_px_gbps = Column(Float, nullable=False, default=0.0)
    data_stream_ms_gbps = Column(Float, nullable=False, default=0.0)
    capture_bandwidth_km = Column(Float, nullable=False, default=0.0)
    maximum_route_length_km = Column(Float, nullable=False, default=0.0)
    length_of_the_information_line_of_the_ccd_matrix = Column(String, nullable=False, default='')
    lens_f_d_mm = Column(String, nullable=False, default='')
    pixel_size = Column(Float, nullable=False, default=0.0)
    platform_id = Column(Integer, nullable=False)
    structure = Column(String(500), nullable=False, default='')
    weight = Column(Float, nullable=False, default=0.0)
    power_consumption_in_standby_mode = Column(Float, nullable=False, default=0.0)
    power_consumption_in_the_high_speed_mode = Column(Float, nullable=False, default=0.0)
    power_consumption_in_the_orbit_correction_mode = Column(Float, nullable=False, default=0.0)
    power_consumption_in_safe_mode = Column(Float, nullable=False, default=0.0)
    power_consumption_in_ca_operational_mode = Column(Float, nullable=False, default=0.0)
    average_power_consumption_per_cycle = Column(Float, nullable=False, default=0.0)
    mdr = Column(Float, nullable=False, default=0.0)
    sac = Column(Float, nullable=False, default=0.0)
    reliability_budget = Column(Float, nullable=False, default=0.0)
    type_platform = Column(Integer, nullable=False, default=0)

    def to_dict(self):
        """
        Converts the attributes of the CAPlatformView instance into a dictionary.
        """
        return {
            'ca_id': self.ca_id,
            'name_of_the_ca': self.name_of_the_ca,
            'number_of_spectral_channels_px': self.number_of_spectral_channels_px,
            'parameters_of_the_panchromatic_channel_nm': self.parameters_of_the_panchromatic_channel_nm,
            'number_of_spectral_channels_ms': self.number_of_spectral_channels_ms,
            'parameters_of_the_red_channel_nm': self.parameters_of_the_red_channel_nm,
            'parameters_of_the_green_channel_nm': self.parameters_of_the_green_channel_nm,
            'parameters_of_the_blue_channel_nm': self.parameters_of_the_blue_channel_nm,
            'parameters_of_the_near_infrared_channel_nm': self.parameters_of_the_near_infrared_channel_nm,
            'adc_bit_depth_bits': self.adc_bit_depth_bits,
            'bit_depth_of_transmitted_information_bits': self.bit_depth_of_transmitted_information_bits,
            'shooting_mode': self.shooting_mode,
            'interface': self.interface,
            'data_stream_px_gbps': self.data_stream_px_gbps,
            'data_stream_ms_gbps': self.data_stream_ms_gbps,
            'capture_bandwidth_km': self.capture_bandwidth_km,
            'maximum_route_length_km': self.maximum_route_length_km,
            'length_of_the_information_line_of_the_ccd_matrix': self.length_of_the_information_line_of_the_ccd_matrix,
            'lens_f_d_mm': self.lens_f_d_mm,
            'pixel_size': self.pixel_size,
            'platform_id': self.platform_id,
            'structure': self.structure,
            'weight': self.weight,
            'power_consumption_in_standby_mode': self.power_consumption_in_standby_mode,
            'power_consumption_in_the_high_speed_mode': self.power_consumption_in_the_high_speed_mode,
            'power_consumption_in_the_orbit_correction_mode': self.power_consumption_in_the_orbit_correction_mode,
            'power_consumption_in_safe_mode': self.power_consumption_in_safe_mode,
            'power_consumption_in_ca_operational_mode': self.power_consumption_in_ca_operational_mode,
            'average_power_consumption_per_cycle': self.average_power_consumption_per_cycle,
            'mdr': self.mdr,
            'sac': self.sac,
            'reliability_budget': self.reliability_budget,
            'type_platform': self.type_platform
        }


class CAParameters(Base):
    """
    Class for CAParameters data.
    """
    __tablename__ = CA_PARAMETERS

    id = Column(Integer, primary_key=True)
    name_of_the_ca = Column(String, nullable=False, default='')
    number_of_spectral_channels_px = Column(Integer, nullable=False, default=0)
    parameters_of_the_panchromatic_channel_nm = Column(String, nullable=False, default='')
    number_of_spectral_channels_ms = Column(Integer, nullable=False, default=0)
    parameters_of_the_red_channel_nm = Column(String, nullable=False, default='')
    parameters_of_the_green_channel_nm = Column(String, nullable=False, default='')
    parameters_of_the_blue_channel_nm = Column(String, nullable=False, default='')
    parameters_of_the_near_infrared_channel_nm = Column(String, nullable=False, default='')
    adc_bit_depth_bits = Column(Integer, nullable=False, default=0)
    bit_depth_of_transmitted_information_bits = Column(Integer, nullable=False, default=0)
    shooting_mode = Column(String, nullable=False, default='')
    interface = Column(String, nullable=False, default='')
    data_stream_px_gbps = Column(Float, nullable=False, default=0.0)
    data_stream_ms_gbps = Column(Float, nullable=False, default=0.0)
    capture_bandwidth_km = Column(Float, nullable=False, default=0.0)
    maximum_route_length_km = Column(Float, nullable=False, default=0.0)
    length_of_the_information_line_of_the_ccd_matrix = Column(String, nullable=False, default='')
    lens_f_d_mm = Column(String, nullable=False, default='')
    pixel_size = Column(Float, nullable=False, default=0.0)

    def to_dict(self):
        """
        Converts the attributes of the CAParameters instance into a dictionary.
        """
        return {
            'id': self.id,
            'name_of_the_ca': self.name_of_the_ca,
            'number_of_spectral_channels_px': self.number_of_spectral_channels_px,
            'parameters_of_the_panchromatic_channel_nm': self.parameters_of_the_panchromatic_channel_nm,
            'number_of_spectral_channels_ms': self.number_of_spectral_channels_ms,
            'parameters_of_the_red_channel_nm': self.parameters_of_the_red_channel_nm,
            'parameters_of_the_green_channel_nm': self.parameters_of_the_green_channel_nm,
            'parameters_of_the_blue_channel_nm': self.parameters_of_the_blue_channel_nm,
            'parameters_of_the_near_infrared_channel_nm': self.parameters_of_the_near_infrared_channel_nm,
            'adc_bit_depth_bits': self.adc_bit_depth_bits,
            'bit_depth_of_transmitted_information_bits': self.bit_depth_of_transmitted_information_bits,
            'shooting_mode': self.shooting_mode,
            'interface': self.interface,
            'data_stream_px_gbps': self.data_stream_px_gbps,
            'data_stream_ms_gbps': self.data_stream_ms_gbps,
            'capture_bandwidth_km': self.capture_bandwidth_km,
            'maximum_route_length_km': self.maximum_route_length_km,
            'length_of_the_information_line_of_the_ccd_matrix': self.length_of_the_information_line_of_the_ccd_matrix,
            'lens_f_d_mm': self.lens_f_d_mm,
            'pixel_size': self.pixel_size
        }
