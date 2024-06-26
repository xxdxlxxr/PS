for _ in range(3):
    number, tmp, cnt = input(), 1, []

    for i in range(7):
        if number[i] == number[i + 1]:
            tmp += 1
        else:
            cnt.append(tmp)
            tmp = 1
            
    cnt.append(tmp)
    print(max(cnt))