"""Coconut Splat"""

# coconut

syllables, players_count = [int(x) for x in input().split()]
fists, ind = [], 0

for i in range(players_count):
    fists.append(str(i + 1) + "F")

while len(fists) > 1:
    ind = int((ind + syllables - 1) % len(fists))
    state = fists[ind][-1]
    player = fists[ind][:-1]

    del fists[ind]

    if state == "F":
        fists.insert(ind, player + "H")
        fists.insert(ind, player + "H")
    elif state == "H":
        fists.insert(ind, player + "P")
        ind += 1

print(int(fists[0][:-1]))
