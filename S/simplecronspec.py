"""Simple Cron Spec"""

# simplecronspec

from sys import stdin

lines = int(stdin.readline())
unique, starts = set(), 0

for i in range(lines):
    line = stdin.readline().split()
    times = []

    for j in range(3):
        if line[j] == "*" and not j:
            times.append(list(range(24)))
        elif line[j] == "*" and j:
            times.append(list(range(60)))
        else:
            line[j] = line[j].split(",")
            times.append([])
            for k in line[j]:
                if "-" in k:
                    times[-1].extend(list(range(int(k[: k.index("-")]), int(k[k.index("-") + 1 :]) + 1)))
                else:
                    times[-1].append(int(k))


    for j in times[0]:
        for k in times[1]:
            for l in times[2]:
                unique.add(j * 60 * 60 + k * 60 + l)

    starts += len(times[0]) * len(times[1]) * len(times[2])

print(len(unique), starts)
