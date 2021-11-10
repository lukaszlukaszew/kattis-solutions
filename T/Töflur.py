"""Töflur"""

from sys import stdin

nums = int(stdin.readline())
numbers = sorted(list(map(int, stdin.readline().split())))

result = 0

for i in range(nums - 1):
    result += (numbers[i] - numbers[i + 1]) ** 2

print(result)
