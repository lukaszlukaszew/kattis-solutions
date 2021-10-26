"""The Owl and the Fox"""

cases = int(input())

for i in range(cases):
    number = input()

    for j in range(len(number) - 1, -1, -1):
        if number[j] != "0":
            print(int(number[:j] + str(int(number[j]) - 1) + number[j + 1:]))
            break
