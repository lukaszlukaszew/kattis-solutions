"""Permutation Encryption"""

# permutationencryption

while True:
    try:
        key = [int(x) - 1 for x in input().split()[1:]]
        message, result = list(input()), []
        if len(message) % len(key):
            message += [
                " ",
            ] * (len(key) - int(len(message) % len(key)))

        for i in range(int(len(message) // len(key))):
            for j in key:
                result.append(message[i * len(key) + j])

        print("'" + "".join(result) + "'")
    except EOFError:
        break
