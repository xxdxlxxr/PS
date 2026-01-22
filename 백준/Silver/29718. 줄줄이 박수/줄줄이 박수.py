N, M = map(int, input().split())
clap, Q = [[0] * (M + 1)], [[0] * (M + 1) for _ in range(N + 1)]

for i in range(N):
    clap_row = [0] + list(map(int, input().split()))
    clap.append(clap_row)

for i in range(1, N + 1):
    for j in range(1, M + 1):
        Q[i][j] = Q[i - 1][j] + Q[i][j - 1] - Q[i - 1][j - 1] + clap[i][j]

A, answer = int(input()), 0

for i in range(len(Q[-1]) - A):
    answer = max(Q[-1][i + A] - Q[-1][i], answer)

print(answer)