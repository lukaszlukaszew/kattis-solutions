"""Weak Vertices"""

# weakvertices

while True:
    size = int(input())

    if size == -1:
        break

    vertices, weak_vertices = {}, []

    for i in range(size):
        vertices[i] = []
        row = [int(x) for x in input().split()]
        for j in range(size):
            if row[j]:
                vertices[i].append(j)

    for k, v in vertices.items():
        counter = False
        for i in v:
            for j in vertices[i]:
                if k in vertices[j]:
                    counter = counter or True

        if not counter:
            weak_vertices.append(k)

    weak_vertices.sort()

    print(*weak_vertices)
