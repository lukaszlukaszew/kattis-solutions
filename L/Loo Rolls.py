"""Loo Rolls"""

# loorolls

l, u = map(int, input().split())
backup = 1

while l % u:
    backup += 1
    u = u - (l % u)

print(backup)
