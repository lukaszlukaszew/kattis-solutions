"""Competitive Arcade Basketball"""

from sys import stdin, stdout
from collections import defaultdict

n, p, m = [int(x) for x in stdin.readline().split()]
points, printed = defaultdict(int), defaultdict(bool)

for i in range(n):
    stdin.readline()

for i in range(m):
    line = stdin.readline().split()
    points[line[0]] += int(line[1])
    if points[line[0]] >= p and not printed[line[0]]:
        stdout.write(line[0] + " wins!" + "\n")
        printed[line[0]] = True

if len(printed) == 0:
    stdout.write("No winner!")
