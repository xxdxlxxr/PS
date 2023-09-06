def solution(board, k):
    return sum(sum((i + j <= k) * board[i][j] for j in range(len(board[0]))) for i in range(len(board)))