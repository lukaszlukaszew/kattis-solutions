"""Batter Up"""

input()
nums = list(filter(lambda x: x != -1, map(int, input().split())))

print(sum(nums) / (len(nums)))
