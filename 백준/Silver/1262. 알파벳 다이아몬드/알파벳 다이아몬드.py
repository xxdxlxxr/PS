N, R1, C1, R2, C2 = map(int, input().split())
alphabet, tmp_1 = ''.join(chr(i) for i in range(ord('a'), ord('a') + 26)), 2 * N - 1

for i in range(R1, R2 + 1):
    for j in range(C1, C2 + 1):
        i %= tmp_1
        j %= tmp_1
        tmp_2 = abs(N - i - 1) + abs(N - j - 1)

        if tmp_2 + 1> N:
            print('.', end='')
        else:
            print(alphabet[tmp_2 % 26], end='')

    print()