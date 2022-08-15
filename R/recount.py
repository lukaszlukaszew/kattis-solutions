"""Recount"""

# recount

from sys import stdin, stdout

candidates = {}

name = stdin.readline()

while name != "***\n":
    candidates[name] = candidates.get(name, 0) + 1
    name = stdin.readline()

if list(candidates.values()).count(max(candidates.values())) > 1:
    stdout.write("Runoff!")
else:
    stdout.write(
        list(candidates.keys())[
            list(candidates.values()).index(max(candidates.values()))
        ]
    )
