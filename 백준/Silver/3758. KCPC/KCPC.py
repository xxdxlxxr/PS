for i in range(int(input())):
    n, k, t, m = map(int, input().split())
    score = [[0 for _ in range(k)] for _ in range(n)]
    submit = [0 for _ in range(n)]
    time = [0 for _ in range(n)]

    for j in range(m):
        tmp = list(map(int, input().split()))
        score[tmp[0] - 1][tmp[1] - 1] = max(score[tmp[0] - 1][tmp[1] - 1], tmp[2])
        submit[tmp[0] - 1] += 1
        time[tmp[0] - 1] = j

    line = [[sum(score[h]), submit[h], time[h], h] for h in range(n)]
    line.sort(key=lambda x: (-x[0], x[1], x[2]))

    for rank in range(n):
        if line[rank][3] + 1 == t:
            print(rank + 1)