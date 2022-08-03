"""Bits"""

# bits

cases = int(input())

for i in range(cases):
    num = input()
    ones = 0

    for j in range(len(num)):
        ones = max(ones, bin(int(num[: j + 1])).count("1"))

    print(ones)
