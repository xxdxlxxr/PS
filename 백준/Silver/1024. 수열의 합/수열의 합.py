N, L = map(int, input().split())

for i in range(L, 101):
    tmp = N / i - (i + 1) / 2

    if int(tmp) == tmp:
        tmp = int(tmp)

        if tmp + 1 >= 0:
            for j in range(tmp + 1, tmp + i + 1):
                print(j, end=" ")

            break
else:
    print(-1)