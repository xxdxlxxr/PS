while 1:
    n = int(input())

    if n == 0:
        break

    print(sorted([input() for _ in range(n)], key=str.lower)[0])