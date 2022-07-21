"""Mult!"""

# mult

nums, num = int(input()), 0

for i in range(nums):
    if num:
        current = int(input())
        if not current % num:
            print(current)
            num = 0
    else:
        num = int(input())
