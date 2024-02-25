import re

D_TYPE_EOP = 1
EOP_FIELDS = ["year", "month", "day", "mjd", "x", "y", "ut1_utc", "lod", "dx", "dy", "x_err", "y_err", "ut1_utc_err", "lod_err", "dx_err", "dy_err"]
RE_PATTERN_EOP = r"(\d{4})\s+(\d{1,2})\s+(\d{1,2})\s+(\d{5})\s+([\d\.-]+)\s+([\d\.-]+)\s+([\d\.-]+)\s+([\d\.-]+)\s+([\d\.-]+)\s+([\d\.-]+)\s+([\d\.-]+)\s+([\d\.-]+)\s+([\d\.-]+)\s+([\d\.-]+)\s+([\d\.-]+)\s+([\d\.-]+)"
RE_EOP_COMPILED = re.compile(RE_PATTERN_EOP)

D_TYPE_SPACE_ENV = 2
SPACE_ENV_FIELDS = ["yyyy", "ddd", "julianday", "f10", "f81c", "s10", "s81c", "m10", "m81c", "y10", "y81c", "ssrc"]
RE_PATTERN_SPACE_ENV = r"\s+(\d{4})\s+(\d{1,3})\s+(\d+\.\d+)\s+([\d\.-]+)\s+([\d\.-]+)\s+([\d\.-]+)\s+([\d\.-]+)\s+([\d\.-]+)\s+([\d\.-]+)\s+([\d\.-]+)\s+([\d\.-]+)\s+(\w+)"
RE_SPACE_ENV_COMPILED = re.compile(RE_PATTERN_SPACE_ENV)

D_TYPE_C20 = 3
C20_FIELDS = ["year", "c20", "delta_c20", "c20_sigma", "delta_J2", "j2_sigma"]
RE_PATTERN_C20 = r"\s+(\d+\.\d+)\s+(-?\d+\.\d+E[+-]\d+)\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)"
RE_C20_COMPILED = re.compile(RE_PATTERN_C20)


TEMP_FILE = "./temp.txt"