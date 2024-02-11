CREATE TABLE data_type (
    id SERIAL PRIMARY KEY,
    source VARCHAR(100) DEFAULT ''
);



CREATE TABLE nsi_data (
    id SERIAL PRIMARY KEY,
    d_type integer not null,
    year VARCHAR(100) DEFAULT '',
    month VARCHAR(100) DEFAULT '',
    day VARCHAR(100) DEFAULT '',
    mjd VARCHAR(100) DEFAULT '',
    x VARCHAR(100) DEFAULT '',
    y VARCHAR(100) DEFAULT '',
    ut1_utc VARCHAR(100) DEFAULT '',
    lod VARCHAR(100) DEFAULT '',
    dx VARCHAR(100) DEFAULT '',
    dy VARCHAR(100) DEFAULT '',
    x_err VARCHAR(100) DEFAULT '',
    y_err VARCHAR(100) DEFAULT '',
    ut1_utc_err VARCHAR(100) DEFAULT '',
    lod_err VARCHAR(100) DEFAULT '',
    dx_err VARCHAR(100) DEFAULT '',
    dy_err VARCHAR(100) DEFAULT '',
    yyyy VARCHAR(100) DEFAULT '',
    ddd VARCHAR(100) DEFAULT '',
    JulianDay VARCHAR(100) DEFAULT '',
    f10 VARCHAR(100) DEFAULT '',
    f81c VARCHAR(100) DEFAULT '',
    s10 VARCHAR(100) DEFAULT '',
    s81c VARCHAR(100) DEFAULT '',
    m10 VARCHAR(100) DEFAULT '',
    m81c VARCHAR(100) DEFAULT '',
    y10 VARCHAR(100) DEFAULT '',
    y81c VARCHAR(100) DEFAULT '',
    ssrc VARCHAR(100) DEFAULT '',
    year_c20 VARCHAR(100) DEFAULT '',
    c20 VARCHAR(100) DEFAULT '',
    delta_c20 VARCHAR(100) DEFAULT '',
    c20_sigma VARCHAR(100) DEFAULT '',
    delta_j2 VARCHAR(100) DEFAULT '',
    j2_sigma VARCHAR(100) DEFAULT '',
    foreign key (d_type) references data_type (id)
);


INSERT INTO data_type (source) VALUES
('EOP_14_C04_IAU2000A_one_file_1962-now'),
('SOLFSMY'),
('C20_Long_Term');



-- TODO add only not empty fields
CREATE VIEW view_set_1 AS
SELECT id, d_type, year, month, day, mjd, x, y, ut1_utc, lod, dx, dy, x_err, y_err, ut1_utc_err, lod_err, dx_err, dy_err
FROM nsi_data;

CREATE VIEW view_set_2 AS
SELECT id, d_type, yyyy, ddd, JulianDay, f10, f81c, s10, s81c, m10, m81c, y10, y81c, ssrc
FROM nsi_data;

CREATE VIEW view_set_3 AS
SELECT id, d_type, year_c20, c20, delta_c20, c20_sigma, delta_j2, j2_sigma
FROM nsi_data;
