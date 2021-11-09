"""Luhn's Checksum Algorithm"""

cases = int(input())

for i in range(cases):
    nums = list(map(int, list(input())))
    k = 2

    while k <= len(nums):
        nums[-k] *= 2
        if nums[-k] > 9:
            nums[-k] = int(str(nums[-k])[0]) + int(str(nums[-k])[1])
        k += 2

    if sum(nums) % 10:
        print("FAIL")
    else:
        print("PASS")
