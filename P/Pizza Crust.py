"""Pizza Crust"""

R, C = map(int, input().split())
print(round(float(R - C) ** 2 / float(R ** 2) * 100, 6))
