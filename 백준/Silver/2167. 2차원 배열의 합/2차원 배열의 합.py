N, M = map(int, input().split())
arr = [(M + 1) * [0]] + [[0] + list(map(int, input().split())) for _ in range(N)]

for i in range(N + 1):
    for j in range(M + 1):
        arr[i][j] += arr[i - 1][j] + arr[i][j - 1] - arr[i - 1][j - 1]

for _ in range(int(input())):
    i, j, x, y = map(int, input().split())

    print(arr[x][y] - arr[x][j - 1] - arr[i - 1][y] + arr[i - 1][j-1])