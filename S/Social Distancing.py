"""Social Distancing"""

# socialdistancing2

S, N = map(int, input().split())
seats = [int(x) for x in input().split()]

result = (seats[0] - 1 + S - seats[-1]) // 2 - (1 if not (seats[0] - 1 + S - seats[-1]) % 2 else 0)

for i, val in enumerate(seats[:-1]):
    result += max((seats[i+1] - val - 1)//2, 0) - (1 if not (seats[i+1]-val - 1) % 2 else 0)

print(result)
