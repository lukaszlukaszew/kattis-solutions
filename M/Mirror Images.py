"""Mirror Images"""

# mirror

cases = int(input())

for i in range(cases):
    R, C = map(int, input().split())
    image = []

    for j in range(R):
        image.append(input())

    print("Test", i + 1)

    for j in image[::-1]:
        print(j[::-1])
