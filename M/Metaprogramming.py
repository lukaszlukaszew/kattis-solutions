"""Metaprogramming"""

# metaprogramming

from sys import stdin

ints = {}

for line in stdin:
    line = line.split()

    if len(line) == 3:
        ints[line[2]] = line[1]
    elif len(line) == 4:
        x = ints.get(line[1], 0)
        y = ints.get(line[3], 0)

        if not (x and y):
            print("undefined")
        else:
            print(str(bool(eval(x + line[2] * (1 + int(line[2] == "=")) + y))).lower())
    else:
        break
