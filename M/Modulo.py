"""Modulo"""

result = []

for i in range(10):
    result.append(int(input()) % 42)

print(len(set(result)))
