"""Broken Calculator"""

result = 1
ops = int(input())

for i in range(ops):
    a, op, b = input().split()

    if op == "+":
        result = (int(a) + int(b)) - result
    elif op == "-":
        result *= int(a) - int(b)
    elif op == "/":
        result = int(((int(a) + (int(a) % 2)) / 2))
    elif op == "*":
        result = (int(a) * int(b)) ** 2

    print(result)
