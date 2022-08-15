"""Dreamer"""

# dreamer

from itertools import permutations
from datetime import date

cases = int(input())

for j in range(cases):
    digits = list(input().replace(" ", ""))
    dates = []

    for i in permutations(digits, 8):
        if int("".join(i[4:])) >= 2000:
            try:
                dates.append(
                    date(int("".join(i[4:])), int("".join(i[2:4])), int("".join(i[:2])))
                )
            except ValueError:
                continue

    try:
        print(
            len(set(dates)),
            str(min(dates).day).zfill(2),
            str(min(dates).month).zfill(2),
            min(dates).year,
        )
    except ValueError:
        print(0)
