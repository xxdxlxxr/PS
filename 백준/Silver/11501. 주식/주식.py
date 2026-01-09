for t in range(int(input())):
    N, price = int(input()), list(map(int, input().split()))
    tmp, answer = 0, 0

    for i in range(len(price) - 1, -1, -1):
        if price[i] > tmp:
            tmp = price[i]
        else:
            answer += tmp - price[i]

    print(answer)