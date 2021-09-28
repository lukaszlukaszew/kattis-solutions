# poor solution, but I don't know re or regex yet
smiles = (":)", ";)", ":-)", ";-)")
s = input()

for i in range(len(s)):
    for j in smiles:
        if s[i:].startswith(j):
            print(i)
