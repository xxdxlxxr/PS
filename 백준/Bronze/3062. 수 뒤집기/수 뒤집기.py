for _ in range(int(input())):
    N = input()
    tmp = str(int(N) + int(''.join(list(reversed(N)))))

    print('YES' if ''.join(list(reversed(tmp))) == tmp else 'NO')