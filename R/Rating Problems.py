"""Rating Problems"""

n, k = map(int, input().split())
summary = 0

for i in range(k):
    summary += int(input())

print((summary + (-3) * (n - k)) / n, (summary + 3 * (n - k)) / n)
