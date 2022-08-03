"""Secure Doors"""

# securedoors

log = int(input())
options = {"entry": "entered", "exit": "exited"}
people = set()

for i in range(log):
    description, name = input().split()
    anomaly, group = 0, len(people)

    if description == "entry":
        people.add(name)
    else:
        people.discard(name)

    if group == len(people):
        anomaly = 1

    print(name, options[description], "(ANOMALY)" * anomaly)
