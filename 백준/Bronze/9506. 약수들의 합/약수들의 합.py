while 1:
    n = int(input())

    if n < 0:
        break

    divisor = [i for i in range(1, n // 2 + 1) if n % i == 0]
    print(f"{n} = {' + '.join(map(str, divisor))}" if sum(divisor) == n else f'{n} is NOT perfect.')