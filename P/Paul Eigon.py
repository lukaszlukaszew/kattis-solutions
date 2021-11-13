"""Paul Eigon"""

x, *y = map(int, input().split())

if (sum(y) // x) % 2:
    print("opponent")
else:
    print("paul")
