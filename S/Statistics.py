"""Statistics"""

import sys

case = 1

try:
    while True:
        nums = list(map(int, input().split()))[1:]
        print(f'Case {case}: {min(nums)} {max(nums)} {max(nums) - min(nums)}')
        case += 1
except EOFError:
    sys.exit()
