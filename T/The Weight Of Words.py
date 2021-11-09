"""The Weight Of Words"""

from string import ascii_lowercase

letters = ascii_lowercase
length, weight = [int(x) for x in input().split()]
result = ""

if 1 <= weight/length <= 26:
    while length:
        result += letters[int(weight/length) - 1]
        weight -= int(weight/length)
        length -= 1
else:
    result = 'impossible'

print(result)
