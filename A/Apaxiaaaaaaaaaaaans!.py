"""Apaxiaaaaaaaaaaaans!"""

# apaxiaaans

word = input()
result = word[:1]

for i in word:
    if i == result[-1]:
        continue

    result += i

print(result)
