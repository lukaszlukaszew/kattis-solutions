"""Detailed Differences"""

# detaileddifferences

cases = int(input())

for i in range(cases):
    upper_line = input()
    lower_line = input()
    result = ""
    for j, val in enumerate(upper_line):
        if val == lower_line[j]:
            result += "."
        else:
            result += "*"

    print(upper_line)
    print(lower_line)
    print(result, "\n")
