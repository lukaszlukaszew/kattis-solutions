"""Pivot"""

from sys import stdin

numbers = int(stdin.readline())
nums = [int(x) for x in stdin.readline().split()]
check = [True for x in range(numbers)]

counter, max_left, min_right = 0, nums[0], nums[-1]

for i in range(1, numbers):
    max_left = max(max_left, nums[i - 1])
    check[i] = check[i] and nums[i] > max_left

for i in range(numbers - 2, -1, -1):
    min_right = min(min_right, nums[i + 1])
    check[i] = check[i] and nums[i] < min_right

print(sum(check))
