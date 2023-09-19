while 1:
    S = input()
    answer = [int(S)]

    if S == '0':
        break

    while answer[-1] > 9:
        tmp = 1

        for num in str(answer[-1]):
            tmp *= int(num)

        answer.append(tmp)

    print(*answer)