"""Triple Texting"""

# tripletexting

line = input()
words = []

for i in range(0, len(line), int(len(line) / 3)):
    words.append(line[i: i + int(len(line) / 3)])

print(words[0] * int(words[0] == words[1]) + words[2] * int(words[0] != words[1]))
