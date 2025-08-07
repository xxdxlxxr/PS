level, N, grades = list(map(int, input().split())), int(input()), []

for i in range(N):
    grade = 0

    for j in range(3):
        abc = list(map(int, input().split()))

        for k in range(3):
            grade += abc[k] * level[k]

    grades.append(grade)

print(max(grades))