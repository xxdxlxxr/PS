N = int(input())
board, answer = [list(input()) for _ in range(N)], [0, 0]

for i in range(N):
    r, c = 0, 0

    for j in range(N):
        if board[i][j] == '.':
            r += 1
        else:
            r = 0

        if r == 2:
            answer[0] += 1

        if board[j][i] == '.':
            c += 1
        else:
            c = 0

        if c == 2:
            answer[1] += 1

print(*answer)