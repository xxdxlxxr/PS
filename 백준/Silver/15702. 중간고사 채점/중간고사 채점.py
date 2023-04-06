N, M = map(int, input().split())
points = list(map(int, input().split()))
scoring = []

for _ in range(M):
    score = list(input().split())
    sum = 0

    for i in range(N):
        if score[i + 1] == 'O':
            sum += points[i]

    scoring.append([sum, 100000 - int(score[0])])

scoring.sort(reverse = True)

print(100000 - scoring[0][1], scoring[0][0])