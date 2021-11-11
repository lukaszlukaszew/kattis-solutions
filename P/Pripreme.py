"""Pripreme"""

numbers = input()
nums = [int(x) for x in input().split()]

if max(nums) > sum(nums) - max(nums):
    result = 2 * max(nums)
else:
    result = sum(nums)

print(result)
