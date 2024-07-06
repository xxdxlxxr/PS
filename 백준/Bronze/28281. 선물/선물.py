N, X = map(int, input().split())
A = list(map(int, input().split()))
print(X * min(A[i] + A[i + 1] for i in range(N - 1)))