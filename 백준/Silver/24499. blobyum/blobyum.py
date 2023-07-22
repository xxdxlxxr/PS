N, K = map(int, input().split())
A = 2 * list(map(int, input().split()))
tmp = answer = sum(A[:K])

for i in range(2 * N - K):
    tmp += A[i + K] - A[i]
    answer = max(tmp, answer)

print(answer)