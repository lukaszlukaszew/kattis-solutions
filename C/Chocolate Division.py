"""Chocolate Division"""

# chocolatedivision

R, C = map(int, input().split())
print(["Beata", "Alf"][(R * C - 1) % 2])
