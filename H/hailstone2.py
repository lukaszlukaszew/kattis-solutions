"""Hailstone Sequences"""

# hailstone2

num, counter = int(input()), 1

while num != 1:
    if num % 2:
        num = 3 * num + 1
    else:
        num /= 2
    counter += 1

print(counter)
