"""Drunk Vigenère"""

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

first_word = input()
second_word = input()
result = ""

for i in range(len(first_word)):
    if i % 2:
        result += alphabet[
            (alphabet.index(first_word[i]) + alphabet.index(second_word[i])) % 26
        ]
    else:
        result += alphabet[
            (alphabet.index(first_word[i]) - alphabet.index(second_word[i])) % 26
        ]

print(result)
