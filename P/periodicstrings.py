"""Periodic Strings"""

# periodicstrings

line = list(input())

for i in range(1, len(line) + 1):
    if i == 1:
        check = set(line)
        if len(check) == 1:
            print(1)
            break
    else:
        if not len(line) % i:
            temp = line[:i]
            check = temp
            for j in range(i - 1):
                temp = [temp[-1]] + temp[:-1]
                check += temp

            check = check * (int(len(line) // len(check)) + 1)
            check = check[: i * int(len(line) // i)]
            if line == check:
                print(i)
                break
