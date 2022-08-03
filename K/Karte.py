"""Karte"""

# karte

suits = ["P", "K", "H", "T"]
cards = [13, 13, 13, 13]

labels = input()
labels = [labels[i: i + 3] for i in range(0, len(labels), 3)]

if len(labels) != len(set(labels)):
    print("GRESKA")
else:
    for i in labels:
        cards[suits.index(i[0])] -= 1
    print(*cards)
