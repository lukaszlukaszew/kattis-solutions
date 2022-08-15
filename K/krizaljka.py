"""Križaljka"""

# krizaljka

horizontal, vertical = input().split()

for i in horizontal:
    if i in vertical:
        h = horizontal.index(i)
        v = vertical.index(i)
        break

for i, val in enumerate(vertical):
    if i == v:
        print(horizontal)
    else:
        print("." * h + val + (len(horizontal) - h - 1) * ".")
