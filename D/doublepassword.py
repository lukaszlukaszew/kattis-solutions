"""Double Password"""

# doublepassword

from functools import reduce

one, two = input(), input()

print(reduce(lambda x, y: x * y, map(lambda x, y: 1 if x == y else 2, one, two)))
