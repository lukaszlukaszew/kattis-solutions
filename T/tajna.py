"""Tajna"""

# tajna

message = input()

R, C = 1, len(message)
divisors = [(R, C)]

while C > R:
    R += 1
    C = len(message) // R
    if C >= R:
        divisors.append((R, C))

while divisors:
    r, c = divisors.pop()
    if r * c == len(message):
        break

matrix = []
for i in range(r):
    for j in range(c):
        matrix.append(message[j * r + i])

print("".join(matrix))
