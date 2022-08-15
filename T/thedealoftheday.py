"""The Deal of the Day"""

# thedealoftheday

from itertools import combinations
from functools import reduce

cards = [int(x) for x in input().split()]
cards_dict, result = {}, 0
deal = int(input())

for i in range(10):
    cards_dict[i] = cards[i]

for i in combinations(cards_dict.keys(), deal):
    result += reduce(lambda x, y: x * y, map(lambda x: cards_dict[x], i))

print(result)
