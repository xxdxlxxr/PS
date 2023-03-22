N, scores, cnt = int(input()), [], 0

for _ in range(N):
    s, t = map(int, input().split())

    scores.append([s, 100000 - t])

scores.sort(reverse = True)

for score in scores[5:]:
    if score[0] == scores[4][0] and score[1] < scores[4][1]:
        cnt += 1

print(cnt)