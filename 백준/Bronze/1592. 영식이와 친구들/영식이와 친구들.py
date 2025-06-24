N, M, L = map(int, input().split())
tmp, cnt, i = N * [0], 0, 0

while tmp[i] < M - 1:
    tmp[i] += 1
    cnt += 1
    i = (i + L) % N if tmp[i] % 2 == 1 else (i - L) % N

print(cnt)