"""The Key to Cryptography"""

from string import ascii_uppercase

letters, plaintext = ascii_uppercase, []
ciphertext = list(input())
key = list(input())

for i, val in enumerate(ciphertext):
    plaintext.append(
        letters[int((letters.index(val) + 26 - letters.index(key[i])) % 26)]
    )
    key.append(plaintext[-1])

print("".join(plaintext))
