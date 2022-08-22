"""Bus Numbers"""

# busnumbers

nums = int(input())
bus_nums = sorted(map(int, input().split()))

result, local = [], []

for i, val in enumerate(bus_nums):
    if not local or (val == local[-1] + 1):
        local.append(val)
    else:
        if len(local) >= 3:
            result.append(f'{local[0]}-{local[-1]}')
        else:
            result.extend(local)

        local = [val]

if len(local) >= 3:
    result.append(f'{local[0]}-{local[-1]}')
else:
    result.extend(local)

print(*result)
