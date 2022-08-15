"""Conquest Campaign"""

# conquestcampaign

from collections import deque

R, C, N = map(int, input().split())

country, conquered = deque(), set()
moves = ((1, 0), (0, 1), (-1, 0), (0, -1))

for i in range(N):
    r, c = map(int, input().split())
    country.append((r, c, 1))
    conquered.add((r, c))

while country:
    r, c, day = country.popleft()

    for i in moves:
        if 1 <= r + i[0] <= R and 1 <= c + i[1] <= C and (r+i[0], c+i[1]) not in conquered:
            country.append((r+i[0], c+i[1], day+1))
            conquered.add((r+i[0], c+i[1]))

print(day)
            