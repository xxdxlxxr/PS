N, X = map(int, input().split())
T = list(map(int, input().split()))

for i in range(X, 202):
    if i > T[(i - X) % N]:
        print((i - X) % N + 1)
        break