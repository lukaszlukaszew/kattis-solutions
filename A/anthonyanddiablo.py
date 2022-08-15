"""Anthony and Diablo"""

# anthonyanddiablo

from math import pi, sqrt

a, n = map(float, input().split())

if sqrt(a * pi * 4) <= n:
    print("Diablo is happy!")
else:
    print("Need more materials!")
