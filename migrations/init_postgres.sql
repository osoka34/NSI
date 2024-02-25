CREATE TABLE data_type (
    id SERIAL PRIMARY KEY,
    source VARCHAR(100) DEFAULT '',
    descr VARCHAR(2000) DEFAULT ''
);

CREATE TABLE request_logs (
    id SERIAL PRIMARY KEY,
    request_time INTEGER DEFAULT 0,
    request_type VARCHAR(100) DEFAULT '',
    request_data VARCHAR(100) DEFAULT '',
    request_result BOOLEAN DEFAULT FALSE,
    request_duration INTEGER DEFAULT 0,
    request_ip VARCHAR(100) DEFAULT '',
    request_user_agent VARCHAR(255) DEFAULT '',
    request_host VARCHAR(100) DEFAULT '',
    request_path VARCHAR(100) DEFAULT '',
    request_query VARCHAR(100) DEFAULT '',
    request_body VARCHAR(255) DEFAULT ''
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


INSERT INTO data_type (source, descr) VALUES
('EOP_14_C04_IAU2000A_one_file_1962-now', 'EARTH ORIENTATION PARAMETER (EOP) PRODUCT CENTER CENTER (PARIS OBSERVATORY)
                      INTERNATIONAL EARTH ROTATION AND REFERENCE SYSTEMS SERVICE
                                    EOP (IERS) 14 C04 TIME SERIES
               Description: https://hpiers.obspm.fr/eoppc/eop/eopc04/C04.guide.pdf
                            contact: christian.bizouard@obspm.fr'),
('SOLFSMY', '# F10, S10, M10, Y10 data release 5_4g (11-Feb-2024 07:38:05.00) by Space Environment Technologies
# Number of records = 10038 with daily and 81-days centered-smoothed data
# F10, S10, M10, and Y10 (81c) have different observation and report times;
to standardize reporting, all values are reported in sfu units at 12UT;
observations are 3-times daily for F10 (20 UT used), every 5 minutes for S10 (daily average used),
twice daily for M10 (7 and 16 UT), and every 1 minute for Y10 (Xrays are each minute while Lya is daily);
for model inputs the values should be used as a daily value between 0-24 UT for a given calendar date;
F10 and S10 are 1-day lagged, M10 is 2-day, and Y10 is 5-day lagged in JB2008;
the 81-day centered values are used with the same respective lag times.
Ssrc has 4 fields (1 for each index): 0 = (F10, S10, M10, Y10) spline-filled if value or missing if no value;
1 = (F10, M10, Y10) derived or measured index, (S10) SOHO/SEM; 2 = (S10) TIMED/SEE v11;
3 = (S10) SOHO gap (daily); 4 = (S10) SOHO gap (average); 5 = (F10) F10 mean (2 surrounding values), (S10) SDO/EVE;
6 = (S10) GOES/EUVS fill-in, (M10) M10 mean (2 surrounding values);
7 = (S10) S10 scaled to match M10 change from previous day;
8 = (S10) SDO/EVE corrections and all S10 tweaked from sat 12388 delta B%, (Y10) UARS/SOLSTICE V18;
9 = (S10) replace original v4.0h data for versions 4.0 and higher, (Y10) UARS/SOLSTICE v19;
A = (S10) TIMED/SEE solar minimum correction;
B = (S10) replace with original v4.0h S10 data for versions 4.0 and higher, (M10) SORCE/SOLSTICE/SIM v9;
C = (S10) SDO/EVE correction, (Y10) GOES XRS; D = (S10) validated TIMED/SEE, (Y10) GOES XRS and SET composite LYA;
E = (S10) S10 composite, (Y10) SET composite LYA; F = (F10, S10, M10, Y10) mean of bordering values'),
('C20_Long_Term', 'TITLE:       Long-term 30-day estimates of C20 from up to 8 SLR satellites

DESCRIPTION: Estimates of C20 and its variations relative to a reference value of -4.8416945732D-04.
             Each estimate is based on 30-days of laser ranging from up to 8 satellites
             The epoch of each estimate is the mid-point of the 30-day span used.
             No de-aliasing or rate model has been applied. The series spans January
             1976 to Present. The variations and the sigmas have been scaled
             by 1E10. The background model is described in the reference given below.
             Both normalized and unnormalized values are provided for convenience.

CONTACT:     J. C. Ries
             Center for Space Research
             The University of Texas at Austin
             Email: ries@csr.utexas.edu

REFERENCE:   Cheng, M., B. D. Tapley, and J. C. Ries (2013), "Deceleration in the Earth''s
             oblateness", J. Geophys. Res., doi:10.1002/jgrb.50058.   ');



CREATE VIEW view_set_1 AS
SELECT id, d_type, year, month, day, mjd, x, y, ut1_utc, lod, dx, dy, x_err, y_err, ut1_utc_err, lod_err, dx_err, dy_err
FROM nsi_data WHERE d_type = 1;

CREATE VIEW view_set_2 AS
SELECT id, d_type, yyyy, ddd, JulianDay, f10, f81c, s10, s81c, m10, m81c, y10, y81c, ssrc
FROM nsi_data WHERE d_type = 2;

CREATE VIEW view_set_3 AS
SELECT id, d_type, year_c20, c20, delta_c20, c20_sigma, delta_j2, j2_sigma
FROM nsi_data WHERE d_type = 3;
