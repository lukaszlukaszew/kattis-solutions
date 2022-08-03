"""Jumbo Javelin"""

# jumbojavelin

from sys import stdin

n = int(stdin.readline())
result = 0

for i in range(n):
    result += int(stdin.readline())

print(result - n + 1)
