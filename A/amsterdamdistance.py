"""Amsterdam Distance"""

# amsterdamdistance

from math import pi

pie_slices, rings, radius = [float(x) for x in input().split()]
ax, ay, bx, by = [int(x) for x in input().split()]

posibilities = []

for i in range(int(rings + 1)):
    y = (abs(ay - i) + abs(by - i)) * (radius / rings)
    x = (abs(ax - bx) / pie_slices) * pi * (radius * i / rings)
    posibilities.append(x + y)

if posibilities:
    print(min(posibilities))
else:
    print(0.0)
