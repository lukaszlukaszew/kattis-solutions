"""Pervasive Heart Monitor"""

# pervasiveheartmonitor

import sys

try:
    while True:
        line = input().split()
        name, records = [], []

        for i, val in enumerate(line):
            try:
                records.append(float(val))
            except ValueError:
                name.append(val)

        print(str(sum(records) / len(records)), " ".join(name))

except EOFError:
    sys.exit()
