"""Coloring Socks"""

# color

from sys import stdin

S, C, K = [int(x) for x in stdin.readline().split()]
socks = sorted(map(int, stdin.readline().split()))

machines, current, minimum = 1, 0, socks[0]

for i in socks:
    if abs(minimum - i) <= K and current < C:
        current += 1
    else:
        minimum = i
        machines += 1
        current = 1

print(machines)
