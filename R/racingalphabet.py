"""Racing Around the Alphabet"""

# racingalphabet

from string import ascii_uppercase
from math import pi

chars = ascii_uppercase + ' \''

for i in range(int(input())):
    aphorism = input()
    time = 0

    for j, char in enumerate(aphorism):
        if j:
            time += min(
                abs(chars.index(char) - chars.index(aphorism[j-1])),
                len(chars) - chars.index(char) + chars.index(aphorism[j-1]),
                len(chars) + chars.index(char) - chars.index(aphorism[j-1])
            )

    print(time * (2 * pi * 30) / 28 / 15 + len(aphorism))
