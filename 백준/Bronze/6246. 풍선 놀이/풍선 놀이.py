N, Q = map(int, input().split())
arr = N * [1]

for _ in range(Q):
    L, I = map(int, input().split())

    for i in range(L - 1, N, I):
        if arr[i]:
            arr[i] = 0

print(sum(arr))