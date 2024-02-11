# Year
# C20
# delta_C20
# C20_sigma
# delta_J2
# J2_sigma
# 1976.04110 - 4.8416958211E-04 - 1.248
# 6.1182
# 3.2377
# 13.6807

import re

filename = "C20_Long_Term.txt"

all_fields = ["Year", "C20", "delta_C20", "C20_sigma", "delta_J2", "J2_sigma"]

# re_pattern = r"\s+(\d{4}\.\d{5})\s+()

re_pattern = r"\s+(\d+\.\d+)\s+(-?\d+\.\d+E[+-]\d+)\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)"

re_compiled = re.compile(re_pattern)

with open(filename, 'r') as file:
    for line in file:
        match = re_compiled.match(line)
        if match:
            values = match.groups()
            parsed_data = dict(zip(all_fields, values))
            print(parsed_data)