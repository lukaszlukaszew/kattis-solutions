"""Reversed Binary Numbers"""

# reversebinary

print(int("0b" + (bin(int(input())).replace("0b", "")).replace("0B", "")[::-1], 2))
