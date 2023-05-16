for _ in range(int(input())):
    N, X = int(input()), list(map(int, input().split()))
    arr, arr[0] = N * [0], X[0]

    for i in range(1, N):
        arr[i] = max(arr[i - 1] + X[i], X[i])

    print(max(arr))