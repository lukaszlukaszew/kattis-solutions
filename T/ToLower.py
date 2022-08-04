"""ToLower"""

# tolower

P, T = map(int, input().split())
counter = []

for i in range(P):
    counter.append(0)
    for j in range(T):
        line = input()
        counter[i] += int(line[1:] == line[1:].lower())

print(counter.count(T))
