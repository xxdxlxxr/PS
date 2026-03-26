N = int(input())
x, y, answer = 0, 0, [['.' for i in range(N)] for i in range(N)]

for d in input():
    if d == 'D':
        if x + 1 < N:
            for j in range(2):
                if answer[x][y] == '-':
                    answer[x][y] ='+'
                elif answer[x][y] == '.':
                    answer[x][y] = '|'

                if j == 0:
                    x += 1
    elif d == 'U':
        if x > 0:
            for j in range(2):
                if answer[x][y] == '-':
                    answer[x][y] ='+'
                elif answer[x][y] == '.':
                    answer[x][y] = '|'

                if j == 0:
                    x -= 1
    elif d == 'R':
        if y + 1 < N:
            for j in range(2):
                if answer[x][y] == '|':
                    answer[x][y] ='+'
                elif answer[x][y] == '.':
                    answer[x][y] = '-'

                if j == 0:
                    y += 1
    else:
        if y > 0:
            for j in range(2):
                if answer[x][y] == '|':
                    answer[x][y] = '+'
                elif answer[x][y] == '.':
                    answer[x][y] = '-'

                if j == 0:
                    y -= 1

for row in range(N):
    print(''.join(answer[row]))