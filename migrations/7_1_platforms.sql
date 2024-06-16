CREATE TABLE ca_parameters (
    id SERIAL PRIMARY KEY,
    name_of_the_ca TEXT NOT NULL,
    number_of_spectral_channels_px INT DEFAULT 0,
    parameters_of_the_panchromatic_channel_nm TEXT DEFAULT '',
    number_of_spectral_channels_ms INT DEFAULT 0,
    parameters_of_the_red_channel_nm TEXT DEFAULT '',
    parameters_of_the_green_channel_nm TEXT DEFAULT '',
    parameters_of_the_blue_channel_nm TEXT DEFAULT '',
    parameters_of_the_near_infrared_channel_nm TEXT DEFAULT '',
    adc_bit_depth_bits INT DEFAULT 0,
    bit_depth_of_transmitted_information_bits INT DEFAULT 0,
    shooting_mode TEXT DEFAULT '',
    interface TEXT DEFAULT '',
    data_stream_px_gbps FLOAT DEFAULT 0.0,
    data_stream_ms_gbps FLOAT DEFAULT 0.0,
    capture_bandwidth_km FLOAT DEFAULT 0.0,
    maximum_route_length_km FLOAT DEFAULT 0.0,
    length_of_the_information_line_of_the_ccd_matrix TEXT DEFAULT '',
    lens_f_d_mm TEXT DEFAULT '',
    pixel_size FLOAT DEFAULT 0.0
);

INSERT INTO ca_parameters (id, name_of_the_ca, number_of_spectral_channels_px, parameters_of_the_panchromatic_channel_nm, number_of_spectral_channels_ms, parameters_of_the_red_channel_nm, parameters_of_the_green_channel_nm, parameters_of_the_blue_channel_nm, parameters_of_the_near_infrared_channel_nm, adc_bit_depth_bits, bit_depth_of_transmitted_information_bits, shooting_mode, interface, data_stream_px_gbps, data_stream_ms_gbps, capture_bandwidth_km, maximum_route_length_km, length_of_the_information_line_of_the_ccd_matrix, lens_f_d_mm, pixel_size) VALUES
(1, 'КА ВДН', 1, '', 4, '', '', '', '', 12, 12, '', 'Serial RapidIO', 11.92, 2.98, 12, 4000, '', '', 0.0),
(2, 'КА ОН', 1, '', 5, '', '', '', '', 14, 14, '', 'Serial RapidIO', 1.3, 1.04, 50, 4000, '', '', 0.0),
(3, 'КА ОН АИСТ', 1, '', 3, '', '', '', '', 8, 8, '', 'Serial RapidIO', 1.24, 0.41, 30, 4000, '', '', 0.0),
(4, 'КА Грифон', 0, '', 4, '450 – 520', '530 –590', '630 – 690', '760 – 900', 12, 12, '', 'CAN-2', 0.0, 0.0, 0.0, 4000, '4900', '1100 / 130', 0.0055);
