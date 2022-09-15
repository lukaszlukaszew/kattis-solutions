"""Doorman"""

# doorman

max_diff = int(input())
line = list(input()[::-1])

counts = {"W": 0, "M": 0}
waiting = None

while line:
    next_one = line.pop()
    if abs(counts["W"] - counts["M"]) == max_diff:
        counts[next_one] += 1
        if abs(counts["W"] - counts["M"]) > max_diff:
            counts[next_one] -= 1
            if waiting is not None:
                break
            waiting = next_one
        else:
            if waiting is not None:
                line.append(waiting)
                waiting = None
    else:
        counts[next_one] += 1

print(sum(counts.values()))
