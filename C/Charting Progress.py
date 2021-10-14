"""Charting Progress"""

import sys

counter = 0

for line in sys.stdin:
    if line == "\n":
        counter = 0
        print()
    else:
        stars = line.count("*")
        length = len(line) - 1
        sys.stdout.write(
            "." * (length - stars - counter) + "*" * stars + "." * counter + "\n"
        )
        counter += stars
