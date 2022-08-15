"""Hardware"""

# hardware

from sys import stdin
from string import digits

number_of_orders = int(stdin.readline())

for i in range(number_of_orders):
    print(stdin.readline().rstrip())
    summary = stdin.readline().split()
    print(*summary)
    to_do, nums, = {n: 0 for n in digits}, 0

    while nums < int(summary[0]):
        line = stdin.readline().split()
        if len(line) == 4:
            for num in range(int(line[1]), int(line[2]) + int(line[3]), int(line[3])):
                nums += 1
                for j in str(num):
                    to_do[j] += 1
        else:
            nums += 1
            for j in line[0]:
                to_do[j] += 1

    for digit in digits:
        print(f'Make {to_do[digit]} digit {digit}')

    print(f'In total {sum(to_do.values())} digit{"s"*int(sum(to_do.values()) > 1)}')
