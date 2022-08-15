"""Mixed Fractions"""

# mixedfractions

nums = list(map(int, input().split()))

while sum(nums):
    print(int(nums[0] // nums[1]), int(nums[0] % nums[1]), "/", nums[1])
    nums = list(map(int, input().split()))
