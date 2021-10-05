"""Counting Clauses"""

clauses, variables = [int(x) for x in input().split()]

for i in range(clauses):
    input()

if clauses >= 8:
    print("satisfactory")
else:
    print("unsatisfactory")
