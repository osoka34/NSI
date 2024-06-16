CREATE OR REPLACE VIEW ca_platform_view AS
SELECT
    ca.id AS ca_id,
    ca.name_of_the_ca,
    ca.number_of_spectral_channels_px,
    ca.parameters_of_the_panchromatic_channel_nm,
    ca.number_of_spectral_channels_ms,
    ca.parameters_of_the_red_channel_nm,
    ca.parameters_of_the_green_channel_nm,
    ca.parameters_of_the_blue_channel_nm,
    ca.parameters_of_the_near_infrared_channel_nm,
    ca.adc_bit_depth_bits,
    ca.bit_depth_of_transmitted_information_bits,
    ca.shooting_mode,
    ca.interface,
    ca.data_stream_px_gbps,
    ca.data_stream_ms_gbps,
    ca.capture_bandwidth_km,
    ca.maximum_route_length_km,
    ca.length_of_the_information_line_of_the_ccd_matrix,
    ca.lens_f_d_mm,
    ca.pixel_size,
    pc.id AS platform_id,
    pc.structure,
    pc.weight,
    pc.power_consumption_in_standby_mode,
    pc.power_consumption_in_the_high_speed_mode,
    pc.power_consumption_in_the_orbit_correction_mode,
    pc.power_consumption_in_safe_mode,
    pc.power_consumption_in_ca_operational_mode,
    pc.average_power_consumption_per_cycle,
    pc.mdr,
    pc.sac,
    pc.reliability_budget,
    pc.type_platform
FROM
    ca_parameters ca
JOIN
    platform_ca pc ON ca.id = pc.type_platform;
