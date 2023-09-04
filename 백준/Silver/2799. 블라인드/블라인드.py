M, N = map(int, input().split())
answer = 5 * [0]

for _ in range(M):
    tmp = N * [0]
    input()

    for _ in range(4):
        lines = input()

        for i in range(N):
            tmp[i] += lines[5 * i + 1] == '*'

    for type in tmp:
        answer[type] += 1

print(*answer)