"""Refrigerator Transport"""

# refrigerator

from math import inf, ceil

pa, ca, pb, cb, n = map(int, input().split())
a, cost, mina, minb = 0, float(inf), 0, 0

while a < n // ca + 1:
    b = ceil((n - a * ca) / cb)
    if pa * a + pb * b < cost:
        mina, minb, cost = a, b, pa * a + pb * b

    a += 1

print(mina, minb, cost)
