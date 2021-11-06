"""Moscow Dream"""

a, b, c, n = map(int, input().split())

if a + b + c >= n >= 3 and a * b * c > 0:
    print("YES")
else:
    print("NO")
