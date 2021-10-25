"""Kafkaesque"""

signatures = int(input())
clerks = []

for i in range(signatures):
    clerks.append(int(input()))

print(len(list(filter(lambda x: clerks[x] > clerks[x + 1], range(signatures - 1)))) + 1)
