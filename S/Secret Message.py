"""Secret Message"""

from math import sqrt

cases = int(input())

for i in range(cases):
    case, result = input(), ""

    matrix = (
        int(sqrt(len(case)) // 1 + 1) if sqrt(len(case)) % 1 else int(sqrt(len(case)))
    )

    case += (matrix ** 2 - len(case)) * "*"

    for j in range(matrix):
        for k in range(matrix - 1, -1, -1):
            result += case[j + k * matrix]

    print(result.replace("*", ""))
