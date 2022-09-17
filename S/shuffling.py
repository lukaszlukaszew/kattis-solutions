"""Shuffling Along"""

# shuffling


def shuffle(starting_deck, num_of_cards, version):
    """Shuffle deck according to specified type"""
    counter = 0

    num = int(num_of_cards / 2)

    if version == "in":
        while True:
            counter += 1
            for j in range(num):
                starting_deck[j][0] = 2 * j + 1
                starting_deck[num + j][0] = 2 * j

            starting_deck.sort()

            if starting_deck == deck:
                break

    elif version == "out":
        num += int(num_of_cards % 2)

        while True:
            counter += 1
            for j in range(num):
                starting_deck[j][0] = 2 * j
                try:
                    starting_deck[num + j][0] = 2 * j + 1
                except IndexError:
                    continue

            starting_deck.sort()

            if starting_deck == deck:
                break

    return counter


cards, shuffle_type = input().split()
deck = []

for i in range(int(cards)):
    deck.append([i, i])

print(shuffle(deck[:], int(cards), shuffle_type))
