"""A Classy Problem"""

from sys import stdin
from collections import defaultdict

translate = {"middle": "2", "lower": "3", "upper": "1"}

cases = int(stdin.readline())

for i in range(cases):
    people = defaultdict(list)
    group = int(stdin.readline())

    for j in range(group):
        name, classes, rest = stdin.readline().split()
        classes = classes.split("-")
        translation = ""
        for k in range(10):
            if classes:
                translation += translate[classes.pop()]
            else:
                translation += "2"

        people[translation].append(name)

    for j in sorted(people.keys()):
        for k in sorted(people[j]):
            print(k[:-1])

    print("=" * 30)
