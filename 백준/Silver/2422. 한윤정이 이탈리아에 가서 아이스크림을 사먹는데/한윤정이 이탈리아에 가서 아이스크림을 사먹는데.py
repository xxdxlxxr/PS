N, M = map(int, input().split())
tmp = [[0 for _ in range(N)] for _ in range(N)]

for i in range(M):
    num_1, num_2 = map(int, input().split())
    tmp[num_1 - 1][num_2 - 1] = 1
    tmp[num_2 - 1][num_1 - 1] = 1

answer = 0

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if not tmp[i][j] and not tmp[i][k] and not tmp[j][k]:
                answer += 1

print(answer)