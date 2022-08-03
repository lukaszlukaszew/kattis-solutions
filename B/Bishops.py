"""Bishops"""

# bishops

import sys

try:
    while True:
        num = int(input())
        print(max(2 * (num - 1), num))
except EOFError:
    sys.exit()
