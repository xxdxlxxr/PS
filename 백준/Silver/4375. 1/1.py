while 1:
    try:
        n = int(input())
    except:
        break

    num, cnt = 1, 1

    while 1:
        if num % n != 0:
            num = num * 10 + 1
            cnt += 1
        else:
            break
    
    print(cnt)