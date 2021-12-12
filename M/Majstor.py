"""Majstor"""

combinations = {
    "RS": 2,
    "PS": 0,
    "SS": 1,
    "RP": 0,
    "SP": 2,
    "PP": 1,
    "SR": 0,
    "PR": 2,
    "RR": 1,
}

R = int(input())
moves = input()
N = int(input())
friends = []

for i in range(N):
    friends.append(input())

actual_points, max_points = 0, 0

for i in range(R):
    for j in range(N):
        actual_points += combinations[moves[i] + friends[j][i]]

for i in range(R):
    possibilities = []
    for j in "SRP":
        points = 0
        for k in range(N):
            points += combinations[j + friends[k][i]]
        possibilities.append(points)
    max_points += max(possibilities)

print(actual_points)
print(max_points)
