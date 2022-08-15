"""Scaling Recipes"""

# recipes

cases = int(input())

for i in range(cases):
    R, P, D = map(int, input().split())
    factor = D / P
    ingredients = []

    for j in range(R):
        ingredients.append(input().split())
        for k in range(1, 3):
            ingredients[j][k] = float(ingredients[j][k])

    for ingredient in ingredients:
        if ingredient[2] == 100:
            ingredient[1] *= factor
            factor = ingredient[1]
            break

    for ingredient in ingredients:
        ingredient[1] = round(factor * ingredient[2] / 100, 1)
        ingredient.pop()

    print("Recipe #", i + 1)
    for ingredient in ingredients:
        print(*ingredient)

    print(40 * "-")
