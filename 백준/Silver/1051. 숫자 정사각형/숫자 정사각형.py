N, M = map(int, input().split())
arr, answer = [list(input()) for i in range(N)], 0

for i in range(N):
    for j in range(M):
        for k in range(min(N, M)):
            if (i + k) < N and (j + k) < M and arr[i][j] == arr[i][j + k] == arr[i + k][j] == arr[i + k][j + k]:
                answer = max(answer, (k + 1) ** 2)
                
print(answer)