"""Spelling Bee"""

from sys import stdin

main_word = stdin.readline().rstrip()
letter = main_word[0]
main_word = set(main_word)
dictionary = int(stdin.readline())

for i in range(dictionary):
    word = stdin.readline().rstrip()
    if letter in word and len(word) >= 4:
        if not set(word) - main_word:
            print(word)
