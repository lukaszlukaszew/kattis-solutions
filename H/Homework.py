"""Homework"""

homework = input().split(";")
problems = len(homework)

for i in homework:
    if "-" in i:
        problem_range = list(map(int, i.split("-")))
        problems += problem_range[1]-problem_range[0]

print(problems)
