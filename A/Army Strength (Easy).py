"""Army Strength (Easy)"""

# armystrengtheasy

from sys import stdin, stdout

cases = int(stdin.readline())
winners = []

for i in range(cases):
    stdin.readline()
    armies = [int(x) for x in stdin.readline().split()]
    godzilla = sorted([int(x) for x in stdin.readline().split()], reverse=True)
    mechagodzilla = sorted([int(x) for x in stdin.readline().split()], reverse=True)

    while len(godzilla) * len(mechagodzilla) != 0:
        if godzilla[-1] < mechagodzilla[-1]:
            godzilla.pop()
        else:
            mechagodzilla.pop()

    if len(godzilla) == 0 and len(mechagodzilla) != 0:
        stdout.write("MechaGodzilla\n")
    elif len(godzilla) != 0 and len(mechagodzilla) == 0:
        stdout.write("Godzilla\n")
    else:
        stdout.write("uncertain\n")
