N, K = map(int, input().split())
G = list(map(int, input().split()))

for i in range(K):
    tmp = 100 * G[i] // N
    G[i] = 1 if tmp <= 4 else 2 if tmp <= 11 else 3 if tmp <= 23 else 4 if tmp <= 40 else 5 if tmp <= 60 else 6 if tmp <= 77 else 7 if tmp <= 89 else 8 if tmp <= 96 else 9

print(*G)