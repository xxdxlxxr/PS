N, L = map(int, input().split())
tmp, cnt = 1, 0

while 1:
    if str(L) not in str(tmp):
        cnt += 1

    if cnt == N:
        break

    tmp += 1

print(tmp)