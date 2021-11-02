"""Disastrous Doubling"""

from sys import stdin

n = stdin.readline()
experiments = map(int, stdin.readline().split())
start = 1

for i, val in enumerate(experiments):
    start *= 2
    start -= val

if start < 0:
    print("error")
else:
    print(int(start % (10 ** 9 + 7)))
