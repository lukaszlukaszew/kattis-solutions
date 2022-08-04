"""Zamka"""

# zamka

minimum = int(input())
maximum = int(input())
summary = int(input())

for j in range(minimum, maximum + 1):
    if sum(map(int, list(str(j)))) == summary:
        print(j)
        break

for j in range(maximum, minimum - 1, -1):
    if sum(map(int, list(str(j)))) == summary:
        print(j)
        break
