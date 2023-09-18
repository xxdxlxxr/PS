N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]
print(sum(abs(xy[i][0] - xy[i + 1][0]) + abs(xy[i][1] - xy[i + 1][1]) for i in range(N - 1)))