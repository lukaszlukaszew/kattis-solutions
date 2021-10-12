"""Autori"""

name = input().split('-')
result = ''

for i, val in enumerate(name):
    result += val[0]

print(result)
