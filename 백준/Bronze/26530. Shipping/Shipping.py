for _ in range(int(input())):
    answer = 0

    for _ in range(int(input())):
        _, cnt, price = input().split()
        answer += float(cnt) * float(price)

    print(f'${answer:.2f}')