"""H to O"""

# htoo

from re import findall


def analyze(mol):
    """Transform string into dictionary"""
    mol = findall(r"\D\d*", mol)

    molecule_dict = {}

    for i in mol:
        if len(i) == 1:
            num = 1
        else:
            num = int(i[1:])

        molecule_dict[i[0]] = molecule_dict.get(i[0], 0) + num

    return molecule_dict


molecule, count = input().split()
desired_molecule = input()

molecule = analyze(molecule)
desired_molecule = analyze(desired_molecule)

result = []

for k, v in desired_molecule.items():
    result.append(int(molecule.get(k, 0) * int(count) // v))

print(min(result))
