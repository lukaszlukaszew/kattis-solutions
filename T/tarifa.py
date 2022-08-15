"""Tarifa"""

# tarifa

X = int(input())
N = int(input())
used = 0

for i in range(N):
    used += int(input())

print(X * (N + 1) - used)
