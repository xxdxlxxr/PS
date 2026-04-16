N = int(input())
board = [input() for _ in range(N)]

if N < 3:
    print('ongoing')
    exit()

for i in range(N - 2):
    for j in range(N - 2):
        if board[i][j] != '.':
            if board[i][j] == board[i + 1][j + 1] == board[i + 2][j + 2]:
                print(board[i][j])
                exit()

for i in range(N - 2):
    for j in range(N - 2):

        if board[i][N - j - 1] != '.':
            if board[i][N - j - 1] == board[i + 1][N - j - 2] == board[i + 2][N - j - 3]:
                print(board[i][N - j - 1])
                exit()

for i in range(N - 2):
    for j in range(N):
        if board[i][j] != '.':
            if board[i][j] == board[i + 1][j] == board[i + 2][j]:
                print(board[i][j])
                exit()

for i in range(N):
    for j in range(N - 2):
        if board[i][j] != '.':
            if board[i][j] == board[i][j + 1] == board[i][j + 2]:
                print(board[i][j])
                exit()

print('ongoing')