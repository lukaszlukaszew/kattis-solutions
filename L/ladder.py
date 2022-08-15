"""Ladder"""

# ladder

import math

h, v = map(int, input().split())
print(int(math.ceil(h / math.sin(math.radians(v)))))
