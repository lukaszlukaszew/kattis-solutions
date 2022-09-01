"""Progressive Scramble"""

# progressivescramble

from string import ascii_lowercase

cases = int(input())
letters = " " + ascii_lowercase


def encrypt_decrypt(text, mode):
    """Encrypt and decrypt text message"""
    text = list((letters.index(x) for x in text))

    if mode == "e":
        for j, val in enumerate(text):
            if j:
                text[j] = int((val + text[j - 1]) % 27)

    elif mode == "d":
        for j, val in enumerate(text):
            if j:
                text[j] = val - sum(text[:j])
                if text[j] < 0:
                    text[j] += int(27 * (-text[j] // 27 + 1))
                text[j] = int(text[j] % 27)

    return list(map(lambda x: letters[x], text))


for i in range(cases):
    line = list(input())
    print("".join(encrypt_decrypt(line[2:], line[0])))
