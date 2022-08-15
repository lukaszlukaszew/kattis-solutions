"""Hot Hike"""

# hothike

days = int(input())
temperatures = list(map(int, input().split()))
result = []

for i in range(days - 2):
    result.append(max(temperatures[i], temperatures[i + 2]))

print(result.index(min(result)) + 1, min(result))
