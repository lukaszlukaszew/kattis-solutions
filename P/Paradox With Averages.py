"""Paradox With Averages"""

from sys import stdin

cases = int(stdin.readline())

for i in range(cases):
    stdin.readline()
    CS, E = [int(x) for x in stdin.readline().split()]

    all_students = []

    while len(all_students) < CS + E:
        all_students += [int(x) for x in stdin.readline().split()]

    cs_students, e_students = all_students[:CS], all_students[CS:]

    counter, avg_cs, avg_e = (
        0,
        sum(cs_students) / len(cs_students),
        sum(e_students) / len(e_students),
    )

    cs_students_to_check = filter(lambda x: avg_cs > x > avg_e, cs_students)

    print(len(list(cs_students_to_check)))
