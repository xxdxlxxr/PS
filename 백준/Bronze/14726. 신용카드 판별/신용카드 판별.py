for _ in range(int(input())):
    number = list(map(int, input()))

    for i in range(8):
        number[-2 * (i + 1)] = 2 * (number[-2 * (i + 1)] - 4) - 1 if number[-2 * (i + 1)] > 4 else 2 * number[-2 * (i + 1)]

    print('F' if sum(number) % 10 else 'T')