"""Grading"""

limits = map(int, input().split())
score = int(input())
grades = "ABCDE"
grade = ""

for i, val in enumerate(limits):
    if score >= val:
        grade = grades[i]
        break

if grade:
    print(grade)
else:
    print("F")
