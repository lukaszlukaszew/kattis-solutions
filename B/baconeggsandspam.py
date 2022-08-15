"""Bacon, Eggs and Spam"""

# baconeggsandspam

orders_number = int(input())

while orders_number:
    menu_items = {}
    for i in range(orders_number):
        order = input().split()

        for j in order[1:]:
            menu_items[j] = menu_items.get(j, []) + [
                order[0],
            ]

    for i in sorted(menu_items.keys()):
        print(i, " ".join(sorted(menu_items[i])))

    print("")

    orders_number = int(input())
