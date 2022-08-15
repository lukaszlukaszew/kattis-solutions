"""Train Boarding"""

# trainboarding

from collections import defaultdict

cars = defaultdict(int)
N, L, P = map(int, input().split())
maximum = 0

for i in range(P):
    pos = int(input())
    car = min(pos // L, N - 1)
    maximum = max(abs(L * (car + 0.5) - pos), maximum)
    cars[car] += 1

print(int(maximum))
print(max(cars.values()))
