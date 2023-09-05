N, M = map(int, input().split())
board, loc = [int(input()) for _ in range(N)], 0

for i in range(M):
    loc += int(input())

    if loc >= N:
        break

    loc += board[loc]

    if loc >= N:
        break

print(i + 1)