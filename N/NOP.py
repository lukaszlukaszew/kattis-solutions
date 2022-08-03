"""NOP"""

# nop

from string import ascii_uppercase

line = list(input())
nop_count, switch = 0, True

while switch:
    for i in range(1, len(line)):
        if line[i] in ascii_uppercase:
            nop_count += ((4 * ((i // 4) + 1)) - i) * int(bool(i % 4))
            line = line[i:]
            break
    else:
        switch = False

print(nop_count)
