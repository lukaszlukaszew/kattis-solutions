"""School Spirit"""

# schoolspirit

students = int(input())
school_score = 0
students_scores, simulated_scores = [], []

for i in range(students):
    students_scores.append(int(input()))

print(sum((students_scores[x] * 0.8 ** x for x in range(students)))/5)

for i in range(students):
    scores_to_check = students_scores[:i] + students_scores[i+1:]
    simulated_scores.append(sum((scores_to_check[x] * 0.8 ** x for x in range(students-1)))/5)

print(sum(simulated_scores)/len(simulated_scores))
