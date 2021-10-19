"""Server"""

n, T = map(int, input().split())
tasks = list(map(int, input().split()))

time, result = 0, 0

for task in tasks:
    time += task
    if time > T:
        break

    result += 1

print(result)
