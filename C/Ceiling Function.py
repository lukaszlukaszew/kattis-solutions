"""Ceiling Function"""

prototypes = []
dirs = ["R", "L"]
n, k = [int(x) for x in input().split()]

for i in range(n):
    tree = {}
    prototype = [int(x) for x in input().split()]

    tree["root"] = prototype[0]

    for j in prototype[1:]:
        branch = dirs[int(j < tree["root"])]

        while tree.get(branch, 0):
            branch += dirs[int(j < tree[branch])]

        tree[branch] = j

    prototypes.append(tuple(sorted(list(tree.keys()))))

print(len(set(prototypes)))
