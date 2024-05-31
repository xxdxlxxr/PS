while 1:
    n, tmp, answer = int(input()), 0, 0

    if n == -1:
        break

    for _ in range(n):
        s, t = map(int, input().split())
        answer += s * (t - tmp)
        tmp = t

    print(answer, 'miles')