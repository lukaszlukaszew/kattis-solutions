"""Tram"""

from sys import stdin

citizens = int(stdin.readline())
answer = 0

for i in range(citizens):
    x, y = [int(x) for x in stdin.readline().split()]
    answer += x - y

print(-answer/citizens)
