"""Pea Soup and Pancakes"""

# peasoup

restaurants = int(input())
chosen = ""

for i in range(restaurants):
    dish_count, name = int(input()), input()
    counter, dishes = 0, []
    for j in range(dish_count):
        dishes.append(input())

    if not chosen:
        for dish in ("pea soup", "pancakes"):
            if dish in dishes:
                counter += 1

        if counter == 2:
            chosen = name

if chosen:
    print(chosen)
else:
    print("Anywhere is fine I guess")
