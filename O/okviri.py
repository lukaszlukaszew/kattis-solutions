"""Okviri"""

# okviri

line = input()
x, y, z = ".", ".", "#"
params = {0: {0: "*", 1: "*"}, 1: {0: "#", 1: "#"}, 2: {0: "#", 1: "*"}}

for i, val in enumerate(line):
    x += f".{params[(i + 1) % 3][0]}.."
    y += f"{params[(i + 1) % 3][0]}.{params[(i + 1) % 3][0]}."
    z += f".{val}.{params[(i + 1) % 3][1]}"

    if (i + 1) % 3 == 2 and i == len(line) - 1:
        z = z[:-1] + "#"

lines = [x, y, z, y, x]

for i in lines:
    print(i)
