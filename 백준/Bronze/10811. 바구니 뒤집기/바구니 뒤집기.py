N, M = map(int, input().split())
answer = [i for i in range(1, N + 1)]

for _ in range(M):
    i, j = map(int, input().split())
    tmp = list(reversed(answer[i - 1:j]))

    for k in range(i - 1, j):
        answer[k] = tmp[k - i + 1]

print(*answer)