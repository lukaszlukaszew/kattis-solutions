"""Digits"""

# digits

from sys import stdin

num = stdin.readline().strip()

while num != "END":
    result = 1
    while num != "1":
        num = str(len(num))
        result += 1
    print(result)
    num = stdin.readline().strip()
