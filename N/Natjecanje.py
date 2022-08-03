"""Natjecanje"""

# natjecanje

T, B, R = [int(x) for x in input().split()]
broken = {int(x) for x in input().split()}
reserve = {int(x) for x in input().split()}
counter = 0

for i in broken:
    for j in reserve:
        if i in (j - 1, j + 1):
            counter += 1
            reserve.discard(j)
            break

print(B - counter)
