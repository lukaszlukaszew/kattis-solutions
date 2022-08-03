"""Frosh Week"""

# froshweek2

input()
tasks = sorted(map(int, input().split()))
breaks = sorted(map(int, input().split()))

x, y = breaks.pop(), tasks.pop()
counter = 0

while True:
    try:
        if x >= y:
            x, y = breaks.pop(), tasks.pop()
            counter += 1
        else:
            y = tasks.pop()
    except IndexError:
        break

print(counter)
