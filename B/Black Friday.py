"""Black Friday"""

participants = int(input())
outcomes = [int(x) for x in input().split()]

outcomes_sorted = outcomes.copy()
outcomes_sorted.sort(reverse=True)

result = None

for i in outcomes_sorted:
    if outcomes.count(i) > 1:
        continue

    result = outcomes.index(i) + 1
    break

if result is None:
    print("none")
else:
    print(result)
