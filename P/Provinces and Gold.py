"""Provinces and Gold"""

G, S, C = map(int, input().split())
points = G * 3 + S * 2 + C
result = []

if points >= 8:
    result.append('Province')
elif points >= 5:
    result.append('Duchy')
elif points >= 2:
    result.append('Estate')

if points >= 6:
    result.append('Gold')
elif points >= 3:
    result.append('Silver')
else:
    result.append('Copper')

print(*result, sep=" or ")
