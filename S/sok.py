"""Sok"""

# sok

bought = list(map(int, input().split()))
cocktail = list(map(int, input().split()))
possible = list(map(lambda x, y: x / y, bought, cocktail))
print(*map(lambda x, y: x - y * min(possible), bought, cocktail))
