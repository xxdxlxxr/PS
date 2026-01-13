N, K, M = map(int, input().split())
A = list(map(int,input().split()))

for _ in range(M):
    i = int(input())

    if i > 0:
        if K <= i:
            K = i - K + 1
    else:
        if K > i + N:
            K = N + i - (K - 1 - N)

print(K)