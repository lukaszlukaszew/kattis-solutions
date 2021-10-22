"""Hay Points"""

from sys import stdin

dictionary = {}
themes, jobs = [int(x) for x in stdin.readline().split()]

for i in range(themes):
    word, value = stdin.readline().split()
    dictionary[word] = int(value)

for i in range(jobs):
    salary = 0

    line = stdin.readline().split()

    while line != ["."]:
        for j in line:
            salary += dictionary.get(j, 0)

        line = stdin.readline().split()

    print(salary)
