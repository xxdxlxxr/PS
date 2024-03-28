for _ in range(int(input())):
    integers = list(map(int, input().split()))
    cnt = sum(n >= 10 for n in integers)

    print(*integers)
    print(['zilch', 'double', 'double-double', 'triple-double'][cnt], end=2 * '\n')