"""Primary Arithmetic"""

num1, num2 = input().split()

while int(num1) + int(num2):
    num1 = num1.zfill(max(len(num1), len(num2)))
    num2 = num2.zfill(max(len(num1), len(num2)))
    counter, carry = 0, 0

    for i in range(len(num1) - 1, -1, -1):
        column = str(int(num1[i]) + int(num2[i]) + carry).zfill(2)
        carry = int(column[0])
        if carry == 1:
            counter += 1

    if counter:
        end = "s" * int(counter > 1)
        print(f"{counter} carry operation{end}.")
    else:
        print("No carry operation.")

    num1, num2 = input().split()
