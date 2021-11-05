"""Video Speedup"""

n, p, k = map(int, input().split())
multi, T = 0, 0

timestamps = list(map(int, input().split()))
timestamps.append(k)
timestamps.insert(0, 0)

while multi <= n:
    T += (timestamps[multi + 1] - timestamps[multi]) * (1 + (multi * p) / 100)
    multi += 1

print(T)
