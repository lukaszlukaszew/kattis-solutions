"""A Different Problem"""

from functools import reduce

while True:
    try:
        print(reduce(lambda a, b: abs(a - b), map(int, input().split())))
    except:
        break
