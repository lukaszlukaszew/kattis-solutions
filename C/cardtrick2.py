"""Card Trick"""

# cardtrick2

from collections import deque

cases = int(input())

for i in range(cases):
    num = int(input())
    variables = "abcdefghijklmnop"
    cards = []
    shuffle = deque()

    for j in range(num):
        cards.append(variables[j])
        shuffle.append(variables[j])

    for j in range(1, num + 1):
        for k in range(j):
            shuffle.append(shuffle.popleft())

        cards[cards.index(shuffle[0])] = j
        shuffle.popleft()

    print(*cards)
