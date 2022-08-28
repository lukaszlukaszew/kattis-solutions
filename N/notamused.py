"""Not Amused"""

# notamused

import sys
from collections import defaultdict

day = 0

try:
    while True:
        line = input().split()

        if line[0] == "OPEN":
            logs = defaultdict(list)
            day += 1
        elif line[0] == "ENTER":
            logs[line[1]].append([int(line[2]), 0])
        elif line[0] == "EXIT":
            logs[line[1]][-1][1] = int(line[2])
        elif line[0] == "CLOSE":
            if day > 1:
                print()

            print("Day " + str(day))

            for name in sorted(logs.keys()):
                duration = 0
                for j in logs[name]:
                    duration += j[1] - j[0]
                print(name + " $" + format(0.1 * duration, ".2f"))

except EOFError:
    sys.exit()
