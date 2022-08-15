"""Simone"""

# simone

N, K = map(int, input().split())
counter = {}
lights = list(map(int, input().split()))
for i in range(1, K+1):
    counter[i] = lights.count(i)

counter = sorted(filter(lambda x: counter[x] == min(counter.values()), counter.keys()))
print(len(counter))
print(*counter)
