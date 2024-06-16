from internal.entity.ca_parameters.model import CAParameters, CAPlatformView
from internal.dto import CAParametersDto, CAPlatformViewDto


def ca_parameters_from_repo_to_dto(ca_parameters: CAParameters) -> CAParametersDto:
    return CAParametersDto(
        id=ca_parameters.id,
        name_of_the_ca=ca_parameters.name_of_the_ca,
        number_of_spectral_channels_px=ca_parameters.number_of_spectral_channels_px,
        parameters_of_the_panchromatic_channel_nm=ca_parameters.parameters_of_the_panchromatic_channel_nm,
        number_of_spectral_channels_ms=ca_parameters.number_of_spectral_channels_ms,
        parameters_of_the_red_channel_nm=ca_parameters.parameters_of_the_red_channel_nm,
        parameters_of_the_green_channel_nm=ca_parameters.parameters_of_the_green_channel_nm,
        parameters_of_the_blue_channel_nm=ca_parameters.parameters_of_the_blue_channel_nm,
        parameters_of_the_near_infrared_channel_nm=ca_parameters.parameters_of_the_near_infrared_channel_nm,
        adc_bit_depth_bits=ca_parameters.adc_bit_depth_bits,
        bit_depth_of_transmitted_information_bits=ca_parameters.bit_depth_of_transmitted_information_bits,
        shooting_mode=ca_parameters.shooting_mode,
        interface=ca_parameters.interface,
        data_stream_px_gbps=ca_parameters.data_stream_px_gbps,
        data_stream_ms_gbps=ca_parameters.data_stream_ms_gbps,
        capture_bandwidth_km=ca_parameters.capture_bandwidth_km,
        maximum_route_length_km=ca_parameters.maximum_route_length_km,
        length_of_the_information_line_of_the_ccd_matrix=ca_parameters.length_of_the_information_line_of_the_ccd_matrix,
        lens_f_d_mm=ca_parameters.lens_f_d_mm,
        pixel_size=ca_parameters.pixel_size
    )


def ca_parameters_from_repo_to_dto_list(params: list[CAParameters]) -> list[CAParametersDto]:
    return [ca_parameters_from_repo_to_dto(c) for c in params]


def ca_parameters_from_dto_to_repo(ca_parameters_dto: CAParametersDto) -> CAParameters:
    return CAParameters(
        id=ca_parameters_dto.id,
        name_of_the_ca=ca_parameters_dto.name_of_the_ca,
        number_of_spectral_channels_px=ca_parameters_dto.number_of_spectral_channels_px,
        parameters_of_the_panchromatic_channel_nm=ca_parameters_dto.parameters_of_the_panchromatic_channel_nm,
        number_of_spectral_channels_ms=ca_parameters_dto.number_of_spectral_channels_ms,
        parameters_of_the_red_channel_nm=ca_parameters_dto.parameters_of_the_red_channel_nm,
        parameters_of_the_green_channel_nm=ca_parameters_dto.parameters_of_the_green_channel_nm,
        parameters_of_the_blue_channel_nm=ca_parameters_dto.parameters_of_the_blue_channel_nm,
        parameters_of_the_near_infrared_channel_nm=ca_parameters_dto.parameters_of_the_near_infrared_channel_nm,
        adc_bit_depth_bits=ca_parameters_dto.adc_bit_depth_bits,
        bit_depth_of_transmitted_information_bits=ca_parameters_dto.bit_depth_of_transmitted_information_bits,
        shooting_mode=ca_parameters_dto.shooting_mode,
        interface=ca_parameters_dto.interface,
        data_stream_px_gbps=ca_parameters_dto.data_stream_px_gbps,
        data_stream_ms_gbps=ca_parameters_dto.data_stream_ms_gbps,
        capture_bandwidth_km=ca_parameters_dto.capture_bandwidth_km,
        maximum_route_length_km=ca_parameters_dto.maximum_route_length_km,
        length_of_the_information_line_of_the_ccd_matrix=ca_parameters_dto.length_of_the_information_line_of_the_ccd_matrix,
        lens_f_d_mm=ca_parameters_dto.lens_f_d_mm,
        pixel_size=ca_parameters_dto.pixel_size
    )


def ca_platform_view_from_repo_to_dto(ca_platform_view: CAPlatformView) -> CAPlatformViewDto:
    return CAPlatformViewDto(
        ca_id=ca_platform_view.ca_id,
        name_of_the_ca=ca_platform_view.name_of_the_ca,
        number_of_spectral_channels_px=ca_platform_view.number_of_spectral_channels_px,
        parameters_of_the_panchromatic_channel_nm=ca_platform_view.parameters_of_the_panchromatic_channel_nm,
        number_of_spectral_channels_ms=ca_platform_view.number_of_spectral_channels_ms,
        parameters_of_the_red_channel_nm=ca_platform_view.parameters_of_the_red_channel_nm,
        parameters_of_the_green_channel_nm=ca_platform_view.parameters_of_the_green_channel_nm,
        parameters_of_the_blue_channel_nm=ca_platform_view.parameters_of_the_blue_channel_nm,
        parameters_of_the_near_infrared_channel_nm=ca_platform_view.parameters_of_the_near_infrared_channel_nm,
        adc_bit_depth_bits=ca_platform_view.adc_bit_depth_bits,
        bit_depth_of_transmitted_information_bits=ca_platform_view.bit_depth_of_transmitted_information_bits,
        shooting_mode=ca_platform_view.shooting_mode,
        interface=ca_platform_view.interface,
        data_stream_px_gbps=ca_platform_view.data_stream_px_gbps,
        data_stream_ms_gbps=ca_platform_view.data_stream_ms_gbps,
        capture_bandwidth_km=ca_platform_view.capture_bandwidth_km,
        maximum_route_length_km=ca_platform_view.maximum_route_length_km,
        length_of_the_information_line_of_the_ccd_matrix=ca_platform_view.length_of_the_information_line_of_the_ccd_matrix,
        lens_f_d_mm=ca_platform_view.lens_f_d_mm,
        pixel_size=ca_platform_view.pixel_size,
        platform_id=ca_platform_view.platform_id,
        structure=ca_platform_view.structure,
        weight=ca_platform_view.weight,
        power_consumption_in_standby_mode=ca_platform_view.power_consumption_in_standby_mode,
        power_consumption_in_the_high_speed_mode=ca_platform_view.power_consumption_in_the_high_speed_mode,
        power_consumption_in_the_orbit_correction_mode=ca_platform_view.power_consumption_in_the_orbit_correction_mode,
        power_consumption_in_safe_mode=ca_platform_view.power_consumption_in_safe_mode,
        power_consumption_in_ca_operational_mode=ca_platform_view.power_consumption_in_ca_operational_mode,
        average_power_consumption_per_cycle=ca_platform_view.average_power_consumption_per_cycle,
        mdr=ca_platform_view.mdr,
        sac=ca_platform_view.sac,
        reliability_budget=ca_platform_view.reliability_budget,
        type_platform=ca_platform_view.type_platform
    )


def ca_platform_view_from_repo_to_dto_list(params: list[CAPlatformView]) -> list[CAPlatformViewDto]:
    return [ca_platform_view_from_repo_to_dto(c) for c in params]


def ca_platform_view_from_dto_to_repo(ca_platform_view_dto: CAPlatformViewDto) -> CAPlatformView:
    return CAPlatformView(
        ca_id=ca_platform_view_dto.ca_id,
        name_of_the_ca=ca_platform_view_dto.name_of_the_ca,
        number_of_spectral_channels_px=ca_platform_view_dto.number_of_spectral_channels_px,
        parameters_of_the_panchromatic_channel_nm=ca_platform_view_dto.parameters_of_the_panchromatic_channel_nm,
        number_of_spectral_channels_ms=ca_platform_view_dto.number_of_spectral_channels_ms,
        parameters_of_the_red_channel_nm=ca_platform_view_dto.parameters_of_the_red_channel_nm,
        parameters_of_the_green_channel_nm=ca_platform_view_dto.parameters_of_the_green_channel_nm,
        parameters_of_the_blue_channel_nm=ca_platform_view_dto.parameters_of_the_blue_channel_nm,
        parameters_of_the_near_infrared_channel_nm=ca_platform_view_dto.parameters_of_the_near_infrared_channel_nm,
        adc_bit_depth_bits=ca_platform_view_dto.adc_bit_depth_bits,
        bit_depth_of_transmitted_information_bits=ca_platform_view_dto.bit_depth_of_transmitted_information_bits,
        shooting_mode=ca_platform_view_dto.shooting_mode,
        interface=ca_platform_view_dto.interface,
        data_stream_px_gbps=ca_platform_view_dto.data_stream_px_gbps,
        data_stream_ms_gbps=ca_platform_view_dto.data_stream_ms_gbps,
        capture_bandwidth_km=ca_platform_view_dto.capture_bandwidth_km,
        maximum_route_length_km=ca_platform_view_dto.maximum_route_length_km,
        length_of_the_information_line_of_the_ccd_matrix=ca_platform_view_dto.length_of_the_information_line_of_the_ccd_matrix,
        lens_f_d_mm=ca_platform_view_dto.lens_f_d_mm,
        pixel_size=ca_platform_view_dto.pixel_size,
        platform_id=ca_platform_view_dto.platform_id,
        structure=ca_platform_view_dto.structure,
        weight=ca_platform_view_dto.weight,
        power_consumption_in_standby_mode=ca_platform_view_dto.power_consumption_in_standby_mode,
        power_consumption_in_the_high_speed_mode=ca_platform_view_dto.power_consumption_in_the_high_speed_mode,
        power_consumption_in_the_orbit_correction_mode=ca_platform_view_dto.power_consumption_in_the_orbit_correction_mode,
        power_consumption_in_safe_mode=ca_platform_view_dto.power_consumption_in_safe_mode,
        power_consumption_in_ca_operational_mode=ca_platform_view_dto.power_consumption_in_ca_operational_mode,
        average_power_consumption_per_cycle=ca_platform_view_dto.average_power_consumption_per_cycle,
        mdr=ca_platform_view_dto.mdr,
        sac=ca_platform_view_dto.sac,
        reliability_budget=ca_platform_view_dto.reliability_budget,
        type_platform=ca_platform_view_dto.type_platform
    )
