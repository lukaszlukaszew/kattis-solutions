"""Death and Taxes"""

# deathtaxes

from sys import stdin

p, q, s, a = 0, 0, 0, 0

while True:
    instr, *nums = stdin.readline().split()
    nums = list(map(int, nums))

    if instr == "sell":
        s -= nums[0]
    elif instr == "buy":
        p = nums[0] * nums[1]
        q = nums[0]
        a = (p + a * s) / (q + s)
        s += q
    elif instr == "split":
        s *= nums[0]
        a /= nums[0]
    elif instr == "merge":
        s //= nums[0]
        a *= nums[0]
    elif instr == "die":
        print(s * (nums[0] - max(0, nums[0] - a) * 0.3))
        break
