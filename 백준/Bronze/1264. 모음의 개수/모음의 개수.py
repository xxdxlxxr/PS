while 1:
    lines = input()

    if lines == '#':
        break

    cnt = 0

    for char in lines:
        if char in 'AEIOUaeiou':
            cnt += 1

    print(cnt)