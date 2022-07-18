"""Eye of Sauron"""

# eyeofsauron

tower = input()
left, right = tower[:tower.index("(")], tower[tower.index(")")+1 : ]

print("correct") if len(left) == len(right) else print("fix")
