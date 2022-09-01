"""Mia"""

# mia

line = list(input().split())

while line != ["0", "0", "0", "0"]:
    players = {1: (line[1] + line[0], line[0] + line[1]), 2: (line[2] + line[3], line[3] + line[2])}
    points = {1: 0, 2: 0}

    for k, v in players.items():
        if "12" in v:
            points[k] += 1000

    if sum(points.values()) == 0:
        for k, v in players.items():
            if v[0] == v[1]:
                points[k] += int(v[0]) * 10

    if sum(points.values()) == 0:
        for k, v in players.items():
            points[k] += max(list(map(int, v)))

    if points[1] > points[2]:
        print("Player 1 wins.")
    elif points[1] == points[2]:
        print("Tie.")
    else:
        print("Player 2 wins.")

    line = list(input().split())
