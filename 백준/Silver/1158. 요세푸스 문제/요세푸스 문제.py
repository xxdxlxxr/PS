N, K = map(int, input().split())
arr, answer, cnt = [i for i in range(1, N + 1)], [], 0

for _ in range(N):
    cnt += K - 1

    if cnt >= len(arr):
        cnt %= len(arr)

    answer.append(arr.pop(cnt))

print('<' + str(answer)[1:-1] + '>')