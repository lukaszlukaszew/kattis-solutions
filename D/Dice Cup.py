"""Dice Cup"""

# dicecup

N, M = map(int, input().split())

for j in range(min(N, M) + 1, max(N, M) + 2):
    print(j)
