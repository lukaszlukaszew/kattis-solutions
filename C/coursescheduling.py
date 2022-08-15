"""Course Scheduling"""

# coursescheduling

from sys import stdin
from collections import defaultdict

courses = int(stdin.readline())
courses_dict = defaultdict(set)

for i in range(courses):
    fname, lname, course = stdin.readline().split()
    courses_dict[course].add(fname + lname)

for i in sorted(courses_dict.keys()):
    print(i, len(courses_dict[i]))
