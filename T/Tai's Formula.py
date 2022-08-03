"""Tai's Formula"""

# taisformula

samples = int(input())
result = 0

for i in range(samples):
    l, h = map(float, input().split())

    if i:
        result += ((h1 + h) / 2) * abs(l1 - l)

    h1, l1 = h, l

print(result / 1000)
