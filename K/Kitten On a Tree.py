"""Kitten On a Tree"""

# kitten

nodes, result = {}, [input()]

line = input().split()

while line != ["-1"]:
    nodes[line[0]] = line[1:]
    line = input().split()

while True:
    for k, v in nodes.items():
        if result[-1] in v:
            result.append(k)
            break
    else:
        print(*result)
        break
