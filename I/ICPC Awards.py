"""ICPC Awards"""

teams = int(input())
winners = []
universities = []

for i in range(teams):
    university, team = input().split()

    if university not in universities:
        winners.append((university, team))
        universities.append(university)

for i in range(12):
    print(*winners[i])
