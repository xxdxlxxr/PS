A, B = map(int, input().split())
K, X = map(int, input().split())

print(min(B, (K + X)) - max(A, K - X) + 1 if max(A, K - X) <= min(B, (K + X)) else 'IMPOSSIBLE')