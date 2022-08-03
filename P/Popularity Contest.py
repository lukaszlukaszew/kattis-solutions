"""Popularity Contest"""

# popularitycontest

N, M = map(int, input().split())
friendships = {}

for i in range(M):
    x, y = map(int, input().split())
    friendships[x] = friendships.get(x, 0) + 1
    friendships[y] = friendships.get(y, 0) + 1

print(*[friendships.get(x, 0) - x for x in range(1, N + 1)])
