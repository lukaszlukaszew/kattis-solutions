"""Character Development"""

from math import factorial

characters = int(input())

relationships = 0

if characters >= 2:
    for i in range(2, characters + 1):
        relationships += factorial(characters) / (
            factorial(i) * factorial(characters - i)
        )

print(int(relationships))
