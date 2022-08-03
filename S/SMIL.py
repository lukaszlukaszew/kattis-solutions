"""SMIL"""

# smil

smiles = (":)", ";)", ":-)", ";-)")
s = input()

for i in range(len(s)):
    for j in smiles:
        if s[i:].startswith(j):
            print(i)
