"""Calories From Fat"""

# calories

multiplier = (9, 4, 4, 4, 7)
end_line = False
day = [0, 0, 0, 0, 0]

while True:
    line = input().split()

    if line[0] == "-" and not end_line:
        end_line = True
        print(str(int(round(day[0] / sum(day) * 100, 0))) + "%")
        day = [0, 0, 0, 0, 0]
        continue
    if line[0] == "-" and end_line:
        break

    percent, calories, end_line = 0, 0, False

    for i in range(5):
        if line[i].endswith("g"):
            line[i] = int(line[i][:-1]) * multiplier[i]
            calories += line[i]
        elif line[i].endswith("C"):
            line[i] = int(line[i][:-1])
            calories += line[i]
        else:
            percent += int(line[i][:-1])

    all_cals = calories * 100 / (100 - percent)

    for i in range(5):
        try:
            day[i] += int(line[i][:-1]) * all_cals / 100
        except TypeError:
            day[i] += line[i]
