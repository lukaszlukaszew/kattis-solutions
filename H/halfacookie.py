"""Half a Cookie"""

# halfacookie

import math as mt

while True:
    try:
        r, x, y = [float(x) for x in input().split()]
        s = mt.sqrt(x ** 2 + y ** 2)

        if r > s:
            area = r ** 2 / 2 * (mt.acos(s / r) * 2 - mt.sin(mt.acos(s / r) * 2))
            area2 = r ** 2 * mt.pi
            print(area2 - area, area)
        else:
            print("miss")
    except EOFError:
        break
