"""Variable Arithmetic"""

# variablearithmetic

variables = {}

while True:
    line = input().replace(" ", "").split("+")

    if line[0] == "0":
        break

    if "=" in line[0]:
        var, value = line[0].split("=")
        variables[var] = value
    else:
        summary = 0
        for i, val in enumerate(line):
            line[i] = variables.get(val, val)

        for i in range(len(line) - 1, -1, -1):
            if line[i].isnumeric():
                summary += int(line[i])
                del line[i]

        if summary:
            line.insert(0, summary)

        print(*line, sep=" + ")
