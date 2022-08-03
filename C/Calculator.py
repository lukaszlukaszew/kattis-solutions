"""Calculator"""

# calculator

import sys

try:
    while True:
        print(format(round(eval(input()), 2), ".2f"))
except EOFError:
    sys.exit()
