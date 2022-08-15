"""Cokolada"""

# cokolada

pieces = int(input())
choc_bar, breaks = 1, 0

while pieces > choc_bar:
    choc_bar *= 2

max_bar = choc_bar

while pieces and pieces != choc_bar:
    choc_bar = int(choc_bar / 2)
    if pieces > choc_bar:
        pieces -= choc_bar
    breaks += 1

print(max_bar, breaks)
