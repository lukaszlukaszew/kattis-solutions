"""All about that base"""

# allaboutthatbase

from sys import stdin
from string import digits, ascii_lowercase

bases = digits + ascii_lowercase + "0"


def convert(to, base):
    """Convert num to desired base"""
    num = 0

    for k, val in enumerate(reversed(to)):
        num += bases.index(val) * base ** k

    return num


cases = int(stdin.readline())

for i in range(cases):
    nums = stdin.readline().rstrip().split()
    start, result, used = "0", "", set()

    for j in range(0, 5, 2):
        for x in nums[j]:
            start = max(start, x)
            used.add(x)

    if used == {"1"} and eval(f"{len(nums[0])}{nums[1]}{len(nums[2])}") == len(nums[4]):
        result += "1"

    for j in range(bases.index(start) + 1, 37):
        num1, num2, num3 = convert(nums[0], j), convert(nums[2], j), convert(nums[4], j)
        if (0 < num1 < 2 ** 32) and (0 < num2 < 2 ** 32) and (0 < num2 < 2 ** 32):
            if eval(str(num1) + nums[1] + str(num2)) == num3:
                result += bases[j]

    if result:
        print(result)
    else:
        print("invalid")
