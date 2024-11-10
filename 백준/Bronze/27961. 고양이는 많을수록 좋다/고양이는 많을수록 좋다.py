N, cnt, cur = int(input()), 1, 1

while cur < N:
    cnt += 1
    cur *= 2

print(cnt - (N == 0))