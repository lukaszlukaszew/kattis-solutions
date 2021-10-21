"""Free Food"""

N = int(input())
result = set()

for i in range(N):
    start, end = map(int, input().split())
    result = result.union(set(range(start, end + 1)))

print(len(result))
