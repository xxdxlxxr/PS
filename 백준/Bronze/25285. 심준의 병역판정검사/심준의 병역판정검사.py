for _ in range(int(input())):
    H, W = map(int, input().split())
    BMI, answer = 10000 * W / H ** 2, 0

    if H < 140.1:
        print(6)
    elif H < 146:
        print(5)
    elif H < 159 or H > 204:
        print(4)
    elif H < 161:
        print(3 if 16 <= BMI < 35 else 4)
    else:
        print(1 if 20 <= BMI < 25 else 2 if 18.5 <= BMI < 30 else 3 if 16 <= BMI < 35 else 4)