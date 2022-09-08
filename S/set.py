"""Set!"""

# set

from itertools import combinations

cards, cards_nums, result = {}, [], []

for i in range(4):
    line = input().split()

    for j in range(3):
        cards[i * 3 + j + 1] = line[j]
        cards_nums.append(i * 3 + j + 1)

comb = combinations(cards_nums, 3)

for i in sorted(comb):
    for j in range(4):
        if cards[i[0]][j] == cards[i[1]][j] == cards[i[2]][j]:
            continue

        if cards[i[0]][j] != cards[i[1]][j] and cards[i[1]][j] != cards[i[2]][j] and cards[i[0]][j] != cards[i[2]][j]:
            continue

        break

    else:
        result.append(i)

if result:
    for i in result:
        print(*i)
else:
    print("no sets")
