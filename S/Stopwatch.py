"""Stopwatch"""

presses = int(input())

if presses % 2:
    print("still running")
else:
    time = 0
    for i in range(presses):
        if i % 2:
            time += int(input()) - start
        else:
            start = int(input())

    print(time)
