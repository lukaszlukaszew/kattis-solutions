"""Smoothie Stand"""

from sys import stdin, maxsize

k, r = map(int, stdin.readline().split())
ingredients = list(map(int, stdin.readline().split()))
price = 0

for i in range(r):
    recipe = list(map(int, stdin.readline().split()))
    count = maxsize
    for j in range(k):
        if recipe[j]:
            count = min(count, int(ingredients[j] // recipe[j]))

    price = max(price, count * recipe[-1])

print(int(price))
