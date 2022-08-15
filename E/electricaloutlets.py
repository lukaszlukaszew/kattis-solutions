"""Electrical Outlets"""

# electricaloutlets

cases = int(input())

for i in range(cases):
    case = [int(x) for x in input().split()]

    print(sum(case[1:]) - case[0] + 1)
