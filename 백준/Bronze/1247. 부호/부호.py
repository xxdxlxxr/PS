for _ in range(3):
    total = sum(int(input()) for i in range(int(input())))
    print('0' if total == 0 else '+' if total > 0 else '-')