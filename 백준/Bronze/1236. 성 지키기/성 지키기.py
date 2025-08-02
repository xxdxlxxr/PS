n, m = map(int, input().split())
tmp = []

for _ in range(n):
    tmp.append(input())

row_cnt, col_cnt = 0, 0

for i in range(n):
    if 'X' not in tmp[i]:
        row_cnt += 1

for j in range(m):
    if "X" not in [tmp[i][j] for i in range(n)]:
        col_cnt += 1

print(max(row_cnt, col_cnt))