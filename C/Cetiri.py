"""Cetiri"""

# cetiri

nums = sorted([int(x) for x in input().split()])
diff = min(nums[1] - nums[0], nums[2] - nums[1])
switch = 0

if diff:
    for i in range(4):
        if min(nums) + diff * i not in nums:
            print(min(nums) + diff * i)
else:
    print(min(nums))
