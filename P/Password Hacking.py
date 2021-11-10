"""Password Hacking"""

count = int(input())
probabilities, result = [], 0

for i in range(count):
    probabilities.append(float(input().split()[1]))

probabilities.sort(reverse=True)

for i, val in enumerate(probabilities):
    result += val * (i + 1)

print(result)
