"""Careful Ascent"""

# carefulascent

x, y = [int(x) for x in input().split()]

shields_count = int(input())
shields = []
road = 0
shilded_road = 0

for i in range(shields_count):
    shields.append(tuple(float(x) for x in input().split()))

for i in shields:
    road += (i[1] - i[0]) * i[2]
    shilded_road += i[1] - i[0]

road += y - shilded_road

print(x / road)
