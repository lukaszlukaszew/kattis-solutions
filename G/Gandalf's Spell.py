"""Gandalf's Spell"""

# gandalfsspell

chars = list(input())
words = input().split()
chars_to_words = {}
words_to_chars = {}

if len(chars) == len(words):
    for c, w in zip(chars, words):
        if chars_to_words.get(c, 0) == words_to_chars.get(w, 0) == 0:
            chars_to_words[c], words_to_chars[w] = w , c
        elif chars_to_words.get(c, 0) != w or words_to_chars.get(w, 0) != c:
            print(False)
            break
    else:
        print(True)
else:
    print(False)
