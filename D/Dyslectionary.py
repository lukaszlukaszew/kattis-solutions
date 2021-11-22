"""Dyslectionary"""

words, length = [], 0
word = input()

try:
    while True:
        if word:
            length = max(length, len(word))
            words.append(word[::-1])
        else:
            words.sort()
            for i in words:
                print(i[::-1].rjust(length))
            print()
            words, length = [], 0

        word = input()

except EOFError:
    words.sort()
    for i in words:
        print(i[::-1].rjust(length))
