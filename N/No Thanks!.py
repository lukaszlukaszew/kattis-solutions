"""No Thanks!"""

from sys import stdin

n = int(stdin.readline())

cards = list(map(int, stdin.readline().split()))
cards.append(max(cards) + 2)
cards.sort()

score, switch = 0, True


for i in range(1, n + 1):
    if switch:
        score += cards[i - 1]
    if cards[i - 1] == cards[i] - 1:
        switch = False
    else:
        switch = True

print(score)
