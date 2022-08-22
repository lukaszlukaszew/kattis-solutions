"""Kleptography"""

# kleptography

from string import ascii_lowercase

key_len, plain_len = map(int, input().split())

key_fragment, ciphertext = list(input()), list(input())
key = ciphertext[:]
plaintext = ciphertext[:]

plaintext[-key_len:] = key_fragment

ciphertext_indexes = [ascii_lowercase.index(x) for x in ciphertext]
plaintext_indexes = [ascii_lowercase.index(x) for x in plaintext]
key_indices = [ascii_lowercase.index(x) for x in key]

for i in range(plain_len - 1, key_len - 1, -1):

    if plaintext_indexes[i] > ciphertext_indexes[i]:
        key_indices[i] = ciphertext_indexes[i] + 26 - plaintext_indexes[i]
        key[i] = ascii_lowercase[key_indices[i]]
    else:
        key[i] = ascii_lowercase[ciphertext_indexes[i] - plaintext_indexes[i]]
        key_indices[i] = ciphertext_indexes[i] - plaintext_indexes[i]

    plaintext_indexes[i - key_len] = key_indices[i]
    plaintext[i - key_len] = key[i]

print("".join(plaintext))
