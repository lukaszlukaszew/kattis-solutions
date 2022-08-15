"""Ultimate Binary Watch"""

# ultimatebinarywatch

nums = [bin(int(x))[2:].zfill(4).replace("1", "*").replace("0", ".") for x in input()]

for i in range(4):
    print(nums[0][i], nums[1][i], " ", nums[2][i], nums[3][i])
