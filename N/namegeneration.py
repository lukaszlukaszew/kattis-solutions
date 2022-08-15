"""Name Generation"""

# namegeneration

from string import ascii_lowercase
from itertools import permutations


vovels = {"a", "e", "i", "o", "u"}
consonants = set(ascii_lowercase).difference(vovels)

N = int(input())

perm = permutations(consonants, 4)

for i in vovels:
    for j in perm:
        if N:
            print(f'{j[0]}{j[1]}{i}{j[2]}{j[3]}')
            N -= 1
        else:
            break
