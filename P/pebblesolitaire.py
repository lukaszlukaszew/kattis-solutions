"""Pebble Solitaire"""

# pebblesolitaire

from re import finditer
from sys import stdin


def check_line(game):
    """Check line for possibilities"""
    checked.add(game)

    for pebble in finditer(r"(?=(oo-))", game):
        queue.append(game[: pebble.start(1)] + "--o" + game[pebble.end(1):])

    for pebble in finditer(r"(?=(-oo))", game):
        queue.append(game[: pebble.start(1)] + "o--" + game[pebble.end(1):])


cases = int(stdin.readline())

for i in range(cases):
    line = stdin.readline().rstrip()
    pebbles = line.count("o")
    queue, checked = [], set()

    check_line(line)

    while queue:
        line = queue.pop()
        pebbles = min(pebbles, line.count("o"))
        if line not in checked:
            check_line(line)

    print(pebbles)
