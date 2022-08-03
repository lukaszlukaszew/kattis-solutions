"""ICPC Team Selection"""

# icpcteamselection

from sys import stdin

cases = int(stdin.readline())

for i in range(cases):
    RESULT = 0
    teams = int(stdin.readline())
    scores = sorted(list(map(int, stdin.readline().split())), reverse=True)

    for j in range(teams):
        RESULT += scores[1 + j * 2]

    print(RESULT)
