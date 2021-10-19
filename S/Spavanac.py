"""Spavanac"""

H, M = map(int, input().split())
result = H * 60 + M

if result >= 45:
    result = result - 45
else:
    result = 24 * 60 - (45 - result)

print(result // 60, result % 60)
