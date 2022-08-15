"""Engineering English"""

# engineeringenglish

import sys
from collections import defaultdict

duplicates = defaultdict(int)

try:
    while True:
        line = input().split()

        for i, val in enumerate(line):
            if duplicates[val.lower()]:
                line[i] = "."

            duplicates[val.lower()] += 1

        print(" ".join(line))

except EOFError:
    sys.exit()
