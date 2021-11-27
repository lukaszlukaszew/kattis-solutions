"""Mountain Biking"""

from math import cos, radians, sqrt
from sys import stdin

N, g = stdin.readline().split()
N, g = int(N), float(g)

Ds, alfas = [], []

for i in range(N):
    D, alfa = [int(x) for x in stdin.readline().split()]
    Ds.append(D)
    alfas.append(alfa)

for i in range(N):
    v = 0

    for j in range(i, N):
        a = g * cos(radians(alfas[j]))

        t = max(
            (-v + sqrt(v ** 2 + 2 * a * Ds[j])) / a,
            (-v - sqrt(v ** 2 + 2 * a * Ds[j])) / a,
        )

        v += a * t

    print(v)
