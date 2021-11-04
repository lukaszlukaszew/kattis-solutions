"""Seven Wonders"""

line = input()
counter = [line.count("T"), line.count("C"), line.count("G")]

print(sum(map(lambda x: x**2, counter)) + min(counter) * 7)
