"""Poker Hand"""

# pokerhand

from collections import Counter

print(max(Counter([x[0] for x in input().split()]).values()))
