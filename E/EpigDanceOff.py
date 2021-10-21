"""EpigDanceOff"""

from sys import stdin
import re

N, M = map(int, input().split())
breaks = set(range(M))

for i in range(N):
    breaks = breaks.intersection(
        {x.start() for x in re.finditer("_", stdin.readline())}
    )

print(len(breaks) + 1)
