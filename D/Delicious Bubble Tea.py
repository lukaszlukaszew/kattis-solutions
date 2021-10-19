"""Delicious Bubble Tea"""

from sys import maxsize

tea_count = int(input())
teas = [int(x) for x in input().split()]
topping_count = int(input())
toppings = [int(x) for x in input().split()]
minimum = maxsize

for i in range(tea_count):
    line = [int(x) for x in input().split()]
    prices = [toppings[j - 1] for j in line[1:]]
    minimum = min(min(prices) + teas[i], minimum)

cash = int(input())

print(int(cash // minimum) - 1 * int(int(cash // minimum) - 1 >= 0))
