"""Architecture"""

RC = input()

first_line = [int(x) for x in input().split()]
second_line = [int(x) for x in input().split()]

if max(first_line) == max(second_line):
    print("possible")
else:
    print("impossible")
