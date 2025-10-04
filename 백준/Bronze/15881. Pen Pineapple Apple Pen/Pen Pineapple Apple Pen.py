n, string, i, cnt = int(input()), list(input()), 0, 0

if n < 4:
    string = '   ' + string

while i < n - 3:
    if string[i] == 'p' and string[i + 1] == 'P' and string[i + 2] == 'A' and string[i + 3] == 'p':
        cnt += 1
        i += 4
    else:
        i += 1

print(cnt)