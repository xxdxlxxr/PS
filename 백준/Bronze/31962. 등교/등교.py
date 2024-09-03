N, X = map(int, input().split())
tmp = []

for _ in range(N):
    S, T = map(int, input().split())

    if S + T <= X:
        tmp.append([S + T, S])

print(sorted(tmp)[-1][1] if tmp else -1)