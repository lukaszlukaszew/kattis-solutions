"""Oktalni"""

# oktalni

binary = input()
binary = "0" * (3 - len(binary) % 3) * int(bool(len(binary) % 3)) + binary
result = ""

for i in range(0, len(binary), 3):
    result += str(int("0b" + binary[i: i + 3], 2))

print(result)
