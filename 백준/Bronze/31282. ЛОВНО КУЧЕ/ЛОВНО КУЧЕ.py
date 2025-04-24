N, M, K = map(int, input().split())
print(N // (K - M) + (N % (K - M) != 0))