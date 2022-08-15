"""Proofs"""

# proofs

from sys import stdin

lines = int(stdin.readline())
conclusions, problem = set(), 0

for i in range(lines):
    assumptions, conclusion = stdin.readline().split("-> ")

    if assumptions:
        for j in assumptions.split():
            if j.rstrip() not in conclusions:
                problem = i + 1
                break

    if problem:
        print(problem)
        break

    conclusions.add(conclusion.rstrip())

else:
    print("correct")
