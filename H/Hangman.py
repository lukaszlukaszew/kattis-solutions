"""Hangman"""

# hangman

word = input()
permutation = input()
letters = set(word)
counter = 0


for i in permutation:
    if i in letters:
        letters.remove(i)
        if not letters:
            print("WIN")
            break
    else:
        counter += 1
        if counter == 10:
            print("LOSE")
            break
