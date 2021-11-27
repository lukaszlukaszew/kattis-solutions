"""Rhyming Slang"""

S = input()
rhymes_count = int(input())
rhymes = set()

for i in range(rhymes_count):
    line = set(input().split())
    for j in line:
        if S.endswith(j):
            rhymes = rhymes.union(line)
            break

phrase_count = int(input())

for i in range(phrase_count):
    line = input()
    result = "NO"
    for j in rhymes:
        if line.endswith(j):
            result = "YES"
            break

    print(result)
