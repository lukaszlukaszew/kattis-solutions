"""Welcome to Code Jam (Easy)"""

# welcomeeasy

from sys import stdin
from collections import deque, defaultdict

cases = int(input())
phrase = "welcome to code jam"

for i in range(cases):
    text = stdin.readline().rstrip()
    indices = defaultdict(list)

    for j, val in enumerate(text):
        indices[val].append(j)

    counter, queue = 0, deque()

    for j in indices["w"]:
        queue.append((0, j))

    while queue:
        a, b = queue.popleft()

        if a == len(phrase) - 1:
            counter += 1
            continue

        for j in filter(lambda x: x > b, indices[phrase[a + 1]]):
            queue.append((a + 1, j))

    print(f"Case #{i+1}: {str(counter).zfill(4)[-4:]}")
