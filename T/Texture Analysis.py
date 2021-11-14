"""Texture Analysis"""

counter = 1
line = input()

while line != "END":
    indices = [i for i, x in enumerate(line) if x == "*"]
    breaks = []

    for i in range(len(indices) - 1):
        breaks.append(indices[i + 1] - indices[i])

    if breaks:
        if max(breaks) == min(breaks):
            result = "EVEN"
        else:
            result = "NOT EVEN"
    else:
        result = "EVEN"

    print(counter, result)
    line = input()
    counter += 1
