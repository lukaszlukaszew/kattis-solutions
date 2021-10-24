"""Event Planning"""

participants, budget, hotels, weeks = [int(x) for x in input().split()]
min_price = 0

for i in range(hotels):
    price = int(input())
    beds = [int(x) for x in input().split()]

    for j in range(weeks):
        if beds[j] >= participants:
            if not min_price or min_price > price:
                min_price = price

if not min_price or min_price * participants > budget:
    print("stay home")
else:
    print(min_price * participants)
