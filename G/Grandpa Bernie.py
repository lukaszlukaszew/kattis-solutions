"""Grandpa Bernie"""

from sys import stdin, stdout
from collections import defaultdict

trips, trips_sorted = defaultdict(list), defaultdict(lambda: True)
trip_count = int(stdin.readline())

for i in range(trip_count):
    line = stdin.readline().split()
    trips[line[0]].append(int(line[1]))

queries_count = int(stdin.readline())

for i in range(queries_count):
    line = stdin.readline().split()
    if trips_sorted[line[0]]:
        trips[line[0]].sort()
        trips_sorted[line[0]] = False

    stdout.write(str(trips[line[0]][int(line[1]) - 1]) + "\n")
