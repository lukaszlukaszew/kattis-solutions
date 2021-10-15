"""Cookie Cutters"""

points = int(input())
x, y = [], []

for i in range(points):
    point = [float(x) for x in input().split()]
    x.append(point[0])
    y.append(point[1])

area = float(input())

basic_area = 0
for i in range(points):
    basic_area += x[i] * (y[int(i - 1)] - y[int((i + 1)) % points])
basic_area = abs(basic_area) / 2

diff = (area / basic_area) ** (1 / 2)
min_x, min_y = min(x), min(y)

for i in range(points):
    print((x[i] - min_x) * diff, (y[i] - min_y) * diff)
