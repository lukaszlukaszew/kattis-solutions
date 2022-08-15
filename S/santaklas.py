"""Santa Klas"""

# santaklas

import math

height, angle = [int(x) for x in input().split()]

if 0 <= angle <= 180:
    print("safe")
else:
    if angle > 270:
        angle = angle - 270
        result = int(height / math.cos(math.radians(angle)))
    elif angle == 270:
        result = height
    else:
        angle = 270 - angle
        result = int(height / math.cos(math.radians(angle)))

    print(result)
