"""Eeny Meeny"""

# eenymeeny

from collections import defaultdict

verse = len(input().split()) - 1
player_count = int(input())
team, players, teams = 0, [], defaultdict(list)

for i in range(player_count):
    players.append(input())

x = int(verse % player_count)

while players:
    teams[int(team % 2)].append(players.pop(x))
    team += 1

    if players:
        x = int((x + verse) % len(players))

for i in range(2):
    print(len(teams[i]))
    for j in teams[i]:
        print(j)
