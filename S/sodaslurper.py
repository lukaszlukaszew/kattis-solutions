"""Soda Surpler"""

# sodaslurper

e, f, c = map(int, input().split())
result, var = 0, e + f

while var // c:
    result += var // c
    var = var // c + var % c

print(result)
