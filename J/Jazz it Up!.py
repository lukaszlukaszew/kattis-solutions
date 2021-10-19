"""Jazz it Up!"""

from math import sqrt

n = int(input())

for m in range(2, n):
    switch = 0
    for i in range(2, int(sqrt(n * m))):
        if not (n * m) % (i ** 2):
            switch = 1
            break

    if switch:
        continue

    break

print(m)
