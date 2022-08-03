""" Daylight Saving Time"""

# dst

cases = int(input())

for i in range(cases):
    rotation, *nums = input().split()
    D, H, M = map(int, nums)
    time = 60 * H + M

    if rotation == "B":
        time = time - D + int(time < D) * 24 * 60

    elif rotation == "F":
        time = time + D - int(time + D >= 24 * 60) * 24 * 60

    print(int(time // 60), int(time % 60))
