N, i = int(input()), 2
arr = sorted([list(map(int, input().split())) for _ in range(N)], key = lambda x: -x[2])

if arr[0][0] == arr[1][0]:
    for i in range(2, N):
        if arr[i][0] != arr[0][0]:
            break

for index in [0, 1, i]:
    print(*arr[index][:2])