def function(r, c):
    for i in range(r, r + 3):
        for j in range(c, c + 3):
            A[i][j] ^= 1
                
N, M = map(int, input().split())
A, B = [list(map(int, input())) for _ in range(N)], [list(map(int, input())) for _ in range(N)]
answer = 0

for i in range(N - 2):
    for j in range(M - 2):
        if A[i][j] != B[i][j]:
            function(i, j)
            answer += 1

print([-1, answer][A == B])