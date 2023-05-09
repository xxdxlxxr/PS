n, m = map(int, input().split())
image, space, cnt = [input() for _ in range(n)], input(), 0

for i in range(n):
    BW = input()

    for j in range(m):
        if image[i][j] == BW[j]:
            cnt += 1

print(cnt)