"""Average Character"""

# averagecharacter

line = list(input())

print(chr(sum(map(ord, line))//len(line)))
