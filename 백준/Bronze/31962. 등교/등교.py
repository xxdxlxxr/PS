N, X = map(int, input().split())
answer = -1

for _ in range(N):
    S, T = map(int, input().split())

    if answer < S and S + T <= X:
        answer = S

print(answer)