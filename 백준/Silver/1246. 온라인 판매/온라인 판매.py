N, M = map(int, input().split())
P, A, answer = sorted(int(input()) for _ in range(M)), 0, 0

for i in range(M):
    cnt = M - i
    total = [N, cnt][N > cnt] * P[i]

    if total > answer:
        answer = total
        A = P[i]

print(A, answer)