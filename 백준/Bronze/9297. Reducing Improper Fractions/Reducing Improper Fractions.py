for i in range(1, int(input()) + 1):
    n, d = map(int, input().split())

    if n // d and n % d:
        print(f'Case {i}: {n // d} {n % d}/{d}')
    elif n % d:
        print(f'Case {i}: {n % d}/{d}')
    else:
        print(f'Case {i}: {n // d}')