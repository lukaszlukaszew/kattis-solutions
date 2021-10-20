"""Keywords"""

from sys import stdin

words_count = int(input())
words = set()

for i in range(words_count):
    words.add(stdin.readline().lower().replace("-", " "))

print(len(words))
