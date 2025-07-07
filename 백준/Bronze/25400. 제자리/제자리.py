N, A, tmp, cnt = int(input()), map(int, input().split()), 1, 0

for j in A:
    if j == tmp:
        tmp += 1
    else:
        cnt += 1

print(cnt)