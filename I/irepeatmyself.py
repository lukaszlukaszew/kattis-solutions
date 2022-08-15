"""I Repeat Myself I Repeat Myself I Repeat"""

# irepeatmyself

from math import ceil

cases = int(input())

for i in range(cases):
    line = input()

    for j in range(1, len(line) + 1):
        prefix = line[:j]
        test = prefix * ceil(len(line) / j)

        if test[: len(line)] == line:
            break

    print(len(prefix))
