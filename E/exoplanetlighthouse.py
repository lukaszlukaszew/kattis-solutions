"""Exoplanet Lighthouse"""

# exoplanetlighthouse

from math import acos

cases = int(input())

for i in range(cases):
    R, h1, h2 = map(float, input().split())
    print(R * (acos(R/(R+h1/1000)) + acos(R/(R+h2/1000))))
