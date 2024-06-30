for _ in range(int(input())):
    n, m = map(int, input().split())
    record = [[0, 0] for _ in range(n + 1)]

    for _ in range(m):
        a, b, p, q = map(int, input().split())

        record[a][0] += p
        record[a][1] += q
        record[b][0] += q
        record[b][1] += p

    Pythagorean = [0 if record[i] == [0, 0] else int(1000 * record[i][0] ** 2 / (record[i][0] ** 2 + record[i][1] ** 2)) for i in range(1, n + 1)]
    print(max(Pythagorean))
    print(min(Pythagorean))