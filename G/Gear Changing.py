"""Gear Changing"""

# gearchanging

N, M, P = map(int, input().split())
C = sorted(list(map(int, input().split())), reverse=True)
D = sorted(list(map(int, input().split())))

changes = []

for i in range(N):
    for j in range(M):
        changes.append(C[i]/D[j])

changes.sort()

for i in range(N * M - 1):
    if (changes[i+1] - changes[i])/changes[i] > P/100:
        print("Time to change gears!")
        break
else:
    print("Ride on!")
