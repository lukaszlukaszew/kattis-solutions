"""Egypt"""

while True:
    nums = sorted(list(map(int, input().split())))

    if sum(nums):
        if nums[0] ** 2 + nums[1] ** 2 == nums[2] ** 2:
            print("right")
        else:
            print("wrong")
    else:
        break
