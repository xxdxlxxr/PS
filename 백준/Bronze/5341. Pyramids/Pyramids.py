while 1:
    n = int(input())

    if n:
        print(sum([i + 1 for i in range(n)]))
    else:
        break