"""Perket"""

# perket

from itertools import combinations

ingredient_count = int(input())
ingredients = []

for i in range(ingredient_count):
    ingredients.append([int(x) for x in input().split()])

minimum = abs(ingredients[0][0]-ingredients[0][1])

for i in range(1, ingredient_count+1):
    for j in combinations(ingredients, i):
        product, summary = 1, 0
        for k in j:
            product, summary = product * k[0], summary + k[1]

        minimum = min(minimum, abs(product - summary))

print(minimum)
