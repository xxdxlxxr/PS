N, D, p = map(int, input().split())
A, cnt = list(map(int, input().split())) + [0], 0

for i in range(N):
    if A[i] > 0:
        tmp = A[i] // D + (A[i] % D != 0)
        A[i] -= tmp * D
        A[i + 1] += int(A[i] * p / 100)
        cnt += tmp

print(cnt)