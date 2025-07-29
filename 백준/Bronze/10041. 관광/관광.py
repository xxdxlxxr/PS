W, H, N = map(int, input().split())
P, answer = [list(map(int, input().split())) for _ in range(N)], 0

for i in range(N - 1):
    X1, Y1 = P[i]
    X2, Y2 = P[i + 1]

    if X1 > X2:
        X1, X2 = X2, X1
        Y1, Y2 = Y2, Y1

    if Y1 > Y2:
        answer += abs(X1 - X2) + abs(Y1 - Y2)
    else:
        answer += max(abs(X1 - X2), abs(Y1 - Y2))

print(answer)