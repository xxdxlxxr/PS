N = int(input())
image, diff = [[input() for _ in range(5)] for _ in range(N)], []

for i in range(N - 1):
    for j in range(i + 1, N):
        cnt = 0

        for row in range(5):
            for col in range(7):
                if image[i][row][col] != image[j][row][col]:
                    cnt += 1

        diff.append([cnt, i, j])

diff.sort()
print(diff[0][1] + 1, diff[0][2] + 1)