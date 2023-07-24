N, Q = map(int, input().split())
arr = [[0, 0, 0]]

for _ in range(N):
    tmp = arr[-1].copy()
    tmp[int(input()) - 1] += 1
    arr.append(tmp)

for _ in range(Q):
    a, b = map(int, input().split())
    answer = [arr[b][i] - arr[a - 1][i] for i in range(3)]

    print(*answer)