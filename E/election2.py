"""Election"""

# election2

from sys import stdin, stdout

candidates, votes = {}, {}

lines = int(stdin.readline())

for i in range(lines):
    candidate = stdin.readline()
    party = stdin.readline()
    candidates[candidate] = party

lines = int(stdin.readline())

for i in range(lines):
    vote = stdin.readline()
    votes[vote] = votes.get(vote, 0) + 1

win = max(votes.values())

if list(votes.values()).count(win) > 1:
    stdout.write("tie")
else:
    for k, v in votes.items():
        if v == win:
            stdout.write(candidates[k])
            break
