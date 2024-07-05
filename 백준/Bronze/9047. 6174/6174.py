for _ in range(int(input())):
    n, cnt = input(), 0

    while n != '6174':
        n = str(int(''.join(sorted(n, reverse=True))) - int(''.join(sorted(n))))

        if int(n) < 1000:
            n = (4 - len(n)) * '0' + n

        cnt += 1

    print(cnt)