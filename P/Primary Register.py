"""Primary Register"""

# register

from functools import reduce

registers = [int(x) for x in input().split()]

num, primes = registers[0], (2, 3, 5, 7, 11, 13, 17, 19)
maximum = reduce(lambda x, y: x * y, primes) - 1

for i in range(1, 8):
    num += registers[i] * reduce(lambda x, y: x * y, primes[:i])

print(maximum - num)
