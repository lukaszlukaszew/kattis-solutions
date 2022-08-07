"""Odd Echo"""

# oddecho

words = int(input())

for i in range(words):
    word = input()
    if (i + 1) % 2:
        print(word)
