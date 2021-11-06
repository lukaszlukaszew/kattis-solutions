"""Joint Attack"""

input()
nums = [int(x) for x in input().split()]

up, down = nums.pop(), 1

while len(nums) > 0:
    up, down = down, up
    up = nums.pop() * down + up

if down == 1:
    print(up)
else:
    print(str(up) + "/" + str(down))
