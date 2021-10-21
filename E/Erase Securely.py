"""Erase Securely"""

bits, check = "01", 0
N = int(input())
line_1 = input()
line_2 = input()

for i, val in line_1:
    check += int(bits[int((bits.index(val) + N) % 2)] == line_2[i])

if check:
    print("Deletion succeeded")
else:
    print("Deletion failed")
