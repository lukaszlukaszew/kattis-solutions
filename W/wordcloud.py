"""Word Cloud"""

# wordcloud

from math import ceil

case = 1

w, words_count = [int(x) for x in input().split()]

while w + words_count:
    words = {}
    row_h, row_w, total_h, maximum = 0, 0, 0, 0

    for i in range(words_count):
        word, occurences = input().split()
        occurences = int(occurences)
        maximum = max(maximum, occurences)
        words[word] = occurences

    for k, v in words.items():
        if v >= 5:
            word_h = 8 + ceil(40 * (v - 4) / (maximum - 4))
            word_w = ceil(9 * len(k) * word_h / 16)
            if row_w + word_w > w:
                row_w, total_h = word_w + 10, total_h + row_h
                row_h = word_h
            else:
                row_w += word_w + 10
                row_h = max(row_h, word_h)

    total_h += row_h

    print(f"CLOUD {case}: {total_h}")
    case += 1
    w, words_count = [int(x) for x in input().split()]
