"""Estimating the Area of a Circle"""

# estimatingtheareaofacircle

from math import pi

r, m, c = map(float, input().split())

while r + m + c:
    print(format(pi * r ** 2, ".5f"), format(4 * r ** 2 * c / m, ".5f"))
    r, m, c = map(float, input().split())
