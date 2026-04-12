paper, dx, dy = [[0 for _ in range(101)] for _ in range(101)], [-1, 1, 0, 0], [0, 0, -1, 1]

for _ in range(int(input())):
    x, y = map(int, input().split())
    answer = 0

    for i in range(10):
        for j in range(10):
            paper[x + i][y + j] = 1

    for i in range(101):
        for j in range(101):
            for k in range(4):
                if paper[i][j] == 1 and paper[i + dx[k]][j + dy[k]] == 0:
                    answer += 1

print(answer)