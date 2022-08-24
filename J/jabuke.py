"""Jabuke"""

# jabuke

vertices = []

gp = {}

for i in range(3):
    vartice = tuple(map(int, input().split()))
    vertices.append(vartice)

triangle_area = (
    abs(
        vertices[0][0] * (vertices[1][1] - vertices[2][1])
        + vertices[1][0] * (vertices[2][1] - vertices[0][1])
        + vertices[2][0] * (vertices[0][1] - vertices[1][1])
    )
    / 2
)


points = int(input())
trees = 0

for i in range(points):
    x, y = map(int, input().split())
    area = (
        abs(
            x * (vertices[1][1] - vertices[2][1])
            + vertices[1][0] * (vertices[2][1] - y)
            + vertices[2][0] * (y - vertices[1][1])
        )
        / 2
    )

    area += (
        abs(
            vertices[0][0] * (y - vertices[2][1])
            + x * (vertices[2][1] - vertices[0][1])
            + vertices[2][0] * (vertices[0][1] - y)
        )
        / 2
    )

    area += (
        abs(
            vertices[0][0] * (vertices[1][1] - y)
            + vertices[1][0] * (y - vertices[0][1])
            + x * (vertices[0][1] - vertices[1][1])
        )
        / 2
    )

    trees += int(area == triangle_area)

print(triangle_area)
print(trees)
