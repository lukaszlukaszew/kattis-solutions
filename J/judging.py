"""Judging Troubles"""

# judging

from sys import stdin
from collections import defaultdict

submissions = int(stdin.readline())

DOMjudge, KATTISjudge = defaultdict(int), defaultdict(int)
result = 0

for i in range(submissions):
    DOMjudge[stdin.readline()] += 1

for i in range(submissions):
    KATTISjudge[stdin.readline()] += 1

for k, v in DOMjudge.items():
    result += min(v, KATTISjudge[k])

print(result)
