"""Sort"""

# sort

from collections import Counter, defaultdict

N, C = [int(x) for x in input().split()]

message = input().split()
message_analyzed = defaultdict(list)
occurences = Counter(message)

for k, v in occurences.items():
    message_analyzed[v].append((message.index(k), k))

result = []

for i in sorted(message_analyzed.keys(), reverse=True):
    for j in sorted(message_analyzed[i]):
        result.extend([j[1]] * i)

print(*result)
