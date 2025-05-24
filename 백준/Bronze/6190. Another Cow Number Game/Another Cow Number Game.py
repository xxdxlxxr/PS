N, cnt = int(input()), 0

while N > 1 :
    if N % 2 == 0:
        N //= 2
    else:
        N = 3 * N + 1

    cnt += 1

print(cnt)