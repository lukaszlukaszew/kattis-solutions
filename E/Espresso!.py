"""Espresso!"""

# espresso

n, s = map(int, input().split())
current, refill = s, 0

for i in range(n):
    order = input()
    if order.endswith("L"):
        order = int(order[:-1]) + 1
    else:
        order = int(order)

    if current < order:
        current, refill = s, refill + 1

    current -= order

print(refill)
