N, M = map(int, input().split())
image = [[0 for _ in range(100)] for _ in range(100)]

for _ in range(N):
    lbx, lby, rtx, rty = map(int, input().split())

    for row in range(lbx - 1, rtx):
        for col in range(lby - 1, rty):
            image[row][col] += 1

print(sum(sum(col > M for col in row) for row in image))