"""Laptop Sticker"""

# laptopsticker

wc, hc, ws, hs = map(int, input().split())

print(int(all([wc - ws >= 2, hc - hs >= 2])))
