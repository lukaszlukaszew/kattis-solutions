"""Broken Swords"""

# brokenswords

swords = int(input())
t_b = 0
l_r = 0

for i in range(swords):
    sword = input()
    t_b += sword[:2].count("0")
    l_r += sword[2:].count("0")

print(
    min(t_b, l_r) // 2, t_b - (min(t_b, l_r) // 2) * 2, l_r - (min(t_b, l_r) // 2) * 2
)
