n, piano, tmp = int(input()), 'CXDXEFXGXAXB', []
tmp = [int(input()) % 12 for i in range(n)]

for i in range(65, 72):
    chr_i = chr(i)
    idx, check = piano.index(chr_i), True

    for j in tmp:
        idx += j
        idx %= 12

        if piano[idx] == 'X':
            check = False
            break

    if check:
        print(f'{chr_i} {piano[idx]}')