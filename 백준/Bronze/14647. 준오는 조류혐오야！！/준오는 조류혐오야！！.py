n, m = map(int, input().split())
bingo, cnt = [input().split() for _ in range(n)], [[], []]

for i in range(n):
    cnt[0].append(''.join(bingo[i]).count('9'))

for j in range(m):
    tmp = 0

    for i in range(n):
        tmp += bingo[i][j].count('9')

    cnt[1].append(tmp)

print(sum(cnt[0]) - max(cnt[0] + cnt[1]))