N, K = map(int, input().split())
scores = []

for _ in range(N):
    score = list(map(int, input().split()))
    scores.append(score[1:] + [score[0]])

    if score[0] == K:
        target = score[1:]

scores.sort(reverse=True)

for i in range(N):
    if scores[i][:-1] == target:
        print(i + 1)
        break