while 1:
    n, m, k = map(int, input().split())
    indep, half = n - m - k, n / 2

    if not n:
        break

    print(-1 if k > half or m + indep <= half else 0 if m > n // 2 else n // 2 - m + 1)