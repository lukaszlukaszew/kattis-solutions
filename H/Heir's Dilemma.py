"""Heir's Dilemma"""

start, stop = [int(x) for x in input().split()]
counter = 0

for i in range(start, stop + 1):
    digits = [int(x) for x in str(i)]

    if 0 in digits or len(digits) != len(set(digits)):
        continue

    if not sum(map(lambda x: i % x, digits)):
        counter += 1

print(counter)
