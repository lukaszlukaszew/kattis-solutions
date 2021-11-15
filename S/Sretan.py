"""Sretan"""

k = int(input())
x, power, result = 0, 1, ""

while k - x - 1 >= 0:
    if ((k - x - 1) % 2 ** power) < (2 ** (power - 1)):
        result += "4"
    else:
        result += "7"

    x += 2**power
    power += 1

print(result[::-1])
