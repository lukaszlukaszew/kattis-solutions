"""A Different Problem"""

# different

from functools import reduce

while True:
    try:
        print(reduce(lambda a, b: abs(a - b), map(int, input().split())))
    except EOFError:
        break
