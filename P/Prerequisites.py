"""Prerequisites?"""

line = list(map(int, input().split()))

while sum(line):
    k, m = line
    result = True
    taken_courses = set(map(int, input().split()))

    for i in range(m):
        category, prerequisites, *courses = map(int, input().split())
        courses = set(courses)
        for course in taken_courses:
            courses.discard(course)

        result = result and (len(courses) <= category - prerequisites)

    if result:
        print("yes")
    else:
        print("no")

    line = list(map(int, input().split()))
