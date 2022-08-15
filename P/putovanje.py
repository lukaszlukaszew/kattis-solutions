"""Putovanje"""

# putovanje

N, C = [int(x) for x in input().split()]
maximum = 0
weights = [int(x) for x in input().split()]

for i in range(N):
    current, total = 0, C
    for j in range(i, N):
        if total - weights[j] >= 0:
            total -= weights[j]
            current += 1

    maximum = max(maximum, current)

print(maximum)
