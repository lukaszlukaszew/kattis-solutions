"""Inquiry I"""

# inquiryi

from sys import stdin

nums = []
num_count = int(stdin.readline())

for i in range(num_count):
    nums.append(int(stdin.readline()))

max_num, left, right = 0, 0, sum(nums)

for i in range(num_count):
    left += nums[i] ** 2
    right -= nums[i]
    max_num = max(max_num, left * right)

print(max_num)
