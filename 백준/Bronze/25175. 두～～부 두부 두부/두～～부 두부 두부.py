N, M, K = map(int, input().split())

print(((M - 1) + (K - 3) % N) % N + 1)