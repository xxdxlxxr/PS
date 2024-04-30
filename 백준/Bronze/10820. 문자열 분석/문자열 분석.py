while 1:
    try:
        s = input()
    except:
        break

    cnt = 4 * [0]

    for char in s:
        if char.islower():
            cnt[0] += 1
        elif char.isupper():
            cnt[1] += 1
        elif char.isnumeric():
            cnt[2] += 1
        else:
            cnt[3] += 1

    print(*cnt)