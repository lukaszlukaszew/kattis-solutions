"""Arm Coordination"""

x, y = map(int, input().split())
r = int(input())

operators = ("-", "+")

for i in range(2):
    for j in range(2):
        print(eval(f"{x}{operators[i]}{r}"), eval(f"{y}{operators[j-i]}{r}"))
