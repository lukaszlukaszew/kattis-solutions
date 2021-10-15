"""Cudoviste"""

R, C = map(int, input().split())
parking = []
cars = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}

for i in range(R):
    parking.append(input())

for i in range(R - 1):
    for j in range(C - 1):
        place = parking[i][j: j + 2] + parking[i + 1][j: j + 2]

        if not place.count("#"):
            cars[place.count("X")] += 1

for i in range(5):
    print(cars[i])
