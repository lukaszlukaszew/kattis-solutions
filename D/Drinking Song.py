"""Drinking Song"""

# drinkingsong

a = int(input())
b = input()

while a:
    e1 = "s" * (a > 1)
    e2 = "s" * (a > 2) + "s" * (a == 1)
    e3 = " on the wall" * (a > 1)
    l1 = "it" * (a == 1) + "one" * (a > 1)
    l2 = "no more" * (a == 1) + f"{a-1}" * (a > 1)

    print(f"{a} bottle{e1} of {b} on the wall, {a} bottle{e1} of {b}.")
    print(f"Take {l1} down, pass it around, {l2} bottle{e2} of {b}{e3}.\n")

    a -= 1
