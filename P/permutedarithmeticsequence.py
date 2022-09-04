"""Permuted Arithmetic Sequence"""

# permutedarithmeticsequence

cases = int(input())

for i in range(cases):
    case = [int(x) for x in input().split()]

    differences = [case[j + 2] - val for j, val in enumerate(case[1:-1])]

    if max(differences) == min(differences):
        print("arithmetic")
        continue

    sorted_case = sorted(case[1:])
    differences = [sorted_case[j + 1] - val for j, val in enumerate(sorted_case[:-1])]

    if max(differences) == min(differences):
        print("permuted arithmetic")
        continue

    print("non-arithmetic")
