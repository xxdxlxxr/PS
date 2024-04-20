while 1:
    n, cur, distance = int(input()), 0, 0

    if n == -1:
        break

    for _ in range(n):
        s, t = map(int, input().split())
        distance += (t - cur) * s
        cur = t

    print(distance, 'miles')