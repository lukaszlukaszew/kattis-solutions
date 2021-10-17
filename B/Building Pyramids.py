"""Building Pyramids"""

blocks = int(input())
height = 0
width = 1

while blocks > 0:
    blocks -= width ** 2
    width += 2
    height += 1

print(height - int(blocks < 0))
