"""Count the Vowels"""

# countthevowels

result = 0

for i in input().lower():
    if i in "aeiou":
        result += 1

print(result)
