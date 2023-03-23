N, A, B, cnt = int(input()), [], [], 0
C = [N * [0] for _ in range(N)]

for _ in range(N):
    A.append(list(map(int, input().split())))

for _ in range(N):
    B.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        for k in range(N):
            if A[i][k] and B[k][j]:
                C[i][j] = 1

for row in C:
    cnt += sum(row)

print(cnt)