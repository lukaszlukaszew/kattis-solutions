"""Reverse Rot"""

# reverserot

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

while True:
    try:
        rotation, line = input().split()
    except ValueError:
        break

    result = ""
    for i in line[::-1]:
        result += chars[(chars.index(i) + int(rotation)) % len(chars)]

    print(result)
