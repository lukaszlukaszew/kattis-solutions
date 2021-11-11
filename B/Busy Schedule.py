"""Busy Schedule"""

cases = int(input())

while cases:
    appointments = []

    for i in range(cases):
        time, morning = input().split()
        h, m = map(int, time.split(":"))
        mins = 60 * int(h % 12) + m + int(morning == "p.m.") * 60 * 12

        appointments.append((mins, time, morning))

    appointments.sort()

    for i in appointments:
        print(i[1], i[2])

    print("")

    cases = int(input())
