"""Functional Fun"""

# functionalfun

import sys

while True:
    try:
        domain = set(sys.stdin.readline().split()[1:])
        codomain = set(sys.stdin.readline().split()[1:])
        cases = int(sys.stdin.readline())
        arguments, values = [], []

        for i in range(cases):
            x, y = sys.stdin.readline().rstrip().split(" -> ")
            arguments.append(x)
            values.append(y)

        if len(arguments) != len(set(arguments)):
            result = "not a function"
        elif set(values) == codomain and len(set(arguments)) == len(codomain):
            result = "bijective"
        elif set(values) == codomain and len(set(values)) < len(values):
            result = "surjective"
        elif len(set(values)) == len(values) and len(values) == len(arguments):
            result = "injective"
        else:
            result = "neither injective nor surjective"

        print(result)

    except ValueError:
        sys.exit()
