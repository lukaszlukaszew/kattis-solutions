"""Knot Knowledge"""

n = input()
to_learn = set(input().split())
learned = set(input().split())

print(to_learn.difference(learned).pop())
