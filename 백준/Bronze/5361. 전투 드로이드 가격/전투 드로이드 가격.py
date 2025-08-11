for _ in range(int(input())):
    ABCDE = list(map(int, input().split()))
    prices = [350.34, 230.9, 190.55, 125.3, 180.9]
    print(f'${sum(ABCDE[i] * prices[i] for i in range(5)):.2f}')