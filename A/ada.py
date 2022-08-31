"""The Calculus of Ada"""

# ada

num_count, *step = [int(x) for x in input().split()]
calculations, counter = {}, 0

while len(set(step)) > 1:
    calculations[counter] = step
    step = []
    for i, val in enumerate(calculations[counter][:-1]):
        step.append(calculations[counter][i + 1] - val)

    counter += 1

calculations[counter] = step

next_num = calculations[counter][-1]

for i in range(counter - 1, -1, -1):
    next_num += calculations[i][-1]

print(counter, next_num)
