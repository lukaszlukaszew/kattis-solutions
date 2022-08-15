"""Exam"""

# exam

answers = int(input())
mine = input()
friends = input()
same = 0

for i, val in enumerate(mine):
    if val == friends[i]:
        same += 1

if answers > same:
    print(same + len(mine) - answers)
else:
    print(answers + len(mine) - same)
