"""Sticky Situation"""

from sys import stdin

stdin.readline()
sticks = sorted(map(int, stdin.readline().split()))
result = "impossible"

for i in range(len(sticks) - 2):
    if (
        sticks[i] + sticks[i + 1] > sticks[i + 2]
        and sticks[i] + sticks[i + 2] > sticks[i + 1]
        and sticks[i + 1] + sticks[i + 2] > sticks[i]
    ):
        result = "possible"
        break

print(result)
