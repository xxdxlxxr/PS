N = int(input())
history, cnt = [list(map(int, input().split())) for _ in range(N)], N * [0]

for i in range(N - 1):
    for j in range(i + 1, N):
        for k in range(5):
            if history[i][k] == history[j][k]:
                cnt[i] += 1
                cnt[j] += 1
                break

print(cnt.index(max(cnt)) + 1)