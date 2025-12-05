N = int(input())
scores, cnt = [int(input()) for _ in range(N)], 0

for i in range(N - 1, 0, -1):
    if scores[i] <= scores[i - 1]:
        cnt += (scores[i - 1] - scores[i] + 1)
        scores[i - 1] = scores[i] - 1

print(cnt)