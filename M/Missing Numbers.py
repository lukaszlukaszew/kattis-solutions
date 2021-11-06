"""Missing Numbers"""

n = int(input())
recited, full_range = [], []

for i in range(n):
    recited.append(int(input()))

recited = set(recited)
full_range = set(range(1, max(recited) + 1))
difference = full_range.difference(recited)

if difference:
    for i in sorted(list(difference)):
        print(i)
else:
    print("good job")
