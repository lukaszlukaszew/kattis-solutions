"""Arrangement"""

rooms = int(input())
teams = int(input())

if teams % rooms == 0:
    x = int(teams / rooms)
    for i in range(rooms):
        print("*" * x)
else:
    capacity = int(teams // rooms)
    teams = teams - rooms * capacity

    for i in range(rooms):
        if teams > 0:
            print("*" * (capacity + 1))
            teams -= 1
        else:
            print("*" * capacity)
