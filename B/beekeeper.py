"""Beekeeper"""

# beekeeper

vowels = ["a", "e", "i", "o", "u", "y"]
word_count = int(input())

while word_count:
    words = []
    values = []

    for i in range(word_count):
        words.append(input())
        value = 0
        for j in vowels:
            value += words[-1].count(j*2)
        values.append(value)

    print(words[values.index(max(values))])
    word_count = int(input())
