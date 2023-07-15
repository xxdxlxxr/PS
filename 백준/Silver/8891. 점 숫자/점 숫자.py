def point(n):
    tot, cnt = 0, 1

    while n > tot:
        tot += cnt
        cnt += 1

    return cnt - tot + n - 1, tot - n + 1

for _ in range(int(input())):
    A, B = map(int, input().split())

    print(sum([i for i in range(1, sum(point(A) + point(B)))]) - point(A)[1] - point(B)[1] + 1)