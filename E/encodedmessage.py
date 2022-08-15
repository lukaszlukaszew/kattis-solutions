"""Encoded Message"""

# encodedmessage

from math import sqrt

cases = int(input())

for i in range(cases):
    message = input()
    side = int(sqrt(len(message)))
    result = ""
    for j in range(side):
        for k in range(side):
            result += message[side * (k + 1) - j - 1]

    print(result)
