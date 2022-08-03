"""Mjehuric"""

# mjehuric

import copy

nums = input().split()
nums_copy = copy.deepcopy(nums)
nums_copy.sort()

while True:
    for i in range(4):
        if nums[i] >= nums[i + 1]:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
            print(*nums)

    if nums_copy == nums:
        break
