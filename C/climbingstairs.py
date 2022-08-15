"""Climbing Stairs"""

# climbingstairs

n, r, k = map(int, input().split())
result = r

if n > k + abs(r - k):
    result += n + int((n - r) % 2)
else:
    result += k + abs(r - k)

print(result)
