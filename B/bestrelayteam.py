"""Best Relay Team"""

# bestrelayteam

from math import inf

runners = int(input())
first, second = {}, []
first_runner, second_runners, total_time = "", set(), float(inf)

for _ in range(runners):
    name, f, s = input().split()
    first[name] = float(f)
    second.append((float(s), name))

second.sort()

for k, v in first.items():
    current_time = v
    group = set()
    for i in range(3):
        if second[i][1] == k:
            current_time += second[3][0]
            group.add(second[3][1])
            continue

        current_time += second[i][0]
        group.add(second[i][1])

    if current_time < total_time:
        first_runner = k
        second_runners = group
        total_time = current_time

print(total_time, first_runner, *second_runners, sep="\n")
