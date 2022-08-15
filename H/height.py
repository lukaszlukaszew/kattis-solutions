"""Height Ordering"""

# height

cases = int(input())

for i in range(cases):
    case, *heights = map(int, input().split())
    ordered, steps = [], 0

    ordered.append(heights.pop(0))

    for j in heights:
        for k, val in enumerate(ordered):
            if j > val and k == len(ordered) - 1:
                ordered.append(j)
            elif j < val:
                steps += len(ordered[k:])
                ordered.insert(k, j)
                break

    print(case, steps)
