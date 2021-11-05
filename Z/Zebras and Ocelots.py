"""Zebras and Ocelots"""

bells = 0
pile = int(input())

for i in range(pile):
    if input() == "O":
        bells += 2 ** (pile - i - 1)

print(bells)
