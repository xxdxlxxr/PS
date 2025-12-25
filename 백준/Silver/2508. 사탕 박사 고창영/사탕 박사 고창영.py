for _ in range(int(input())):
    input()
    r, c = map(int, input().split())
    tmp, cnt = [input() for _ in range(r)], 0

    for i in range(r):
        for j in range(c - 2):
            if tmp[i][j] == '>' and tmp[i][j+1] == 'o' and tmp[i][j+2] == '<':
                cnt += 1

    for i in range(r - 2):
        for j in range(c):
            if tmp[i][j] == 'v' and tmp[i+1][j] == 'o' and tmp[i+2][j] == '^':
                cnt += 1

    print(cnt)