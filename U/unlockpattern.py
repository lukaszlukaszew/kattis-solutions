"""Unlock Pattern"""

# unlockpattern

from math import sqrt

pattern, lenght = [], 0

for i in range(3):
    pattern.extend(list(map(int, input().split())))

for i in range(1, 9):
    x = abs(pattern.index(i) % 3 - pattern.index(i + 1) % 3)
    y = abs(pattern.index(i) // 3 - pattern.index(i + 1) // 3)
    lenght += sqrt(x ** 2 + y ** 2)

print(lenght)
