N = int(input())
answer = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    row = input()

    for j in range(N):
        col = row[j]

        if col == '.':
            continue
        
        cnt = int(col)
        answer[i][j] = '*'
        k = 0 if i < 1 else i - 1
        l = N - 1 if N < i + 2 else i + 1
        m = 0 if j < 1 else j - 1
        n = N - 1 if N < j + 2 else j + 1

        for o in range(k, l + 1):
            for p in range(m, n + 1):
                tmp = answer[o][p]
                
                if tmp == '*' or tmp == 'M':
                    continue
                
                if cnt + tmp > 9:
                    answer[o][p] = 'M'
                else:
                    answer[o][p] += cnt

for map_row in answer:
    print(''.join(map(str, map_row)))