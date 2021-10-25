"""Last Factorial Digit"""

from math import factorial

cases = int(input())

for i in range(cases):
    print(str(factorial(int(input())))[-1])
