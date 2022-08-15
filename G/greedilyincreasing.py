"""Greedily Increasing Subsequence"""

# greedilyincreasing

from sys import stdin

stdin.readline()
nums = [int(x) for x in stdin.readline().split()]
current, result = 0, []

for i in nums:
    if i > current:
        result.append(i)
        current = i

print(len(result))
print(*result)
