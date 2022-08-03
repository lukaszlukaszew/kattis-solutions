"""Problem Classification"""

# problemclassification

from sys import stdin
from collections import Counter

keywords, result = {}, {}
categories = int(stdin.readline())

for i in range(categories):
    keyword, *words = stdin.readline().split()
    keywords[keyword] = set(words)

text = Counter()
line = stdin.readline().split()

while line:
    text.update(line)
    line = stdin.readline().split()

for k, v in keywords.items():
    result[k] = sum(map(lambda x: text[x], v))

keys = sorted(filter(lambda x: result[x] == max(result.values()), result.keys()))

for key in keys:
    print(key)
