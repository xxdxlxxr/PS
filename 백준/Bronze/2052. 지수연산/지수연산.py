answer = '%.300f' % (1 / pow(2, int(input())))

for i in range(len(answer) - 1, 1, -1):
    if answer[i] != '0':
        break

print(answer[:i + 1])