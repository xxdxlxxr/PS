n = int(input())

if n > 0:
    F = [0, 1]

    for i in range(n - 1):
        F.append((F[-2] + F[-1]) % 10 ** 9)

    print(1)
    print(F[-1])
elif n < 0:
    F = [1, 0, 1]

    for i in range(-(n + 1)):
        F.append((F[-2] + F[-1]) % 10 ** 9)

    print(2 * (-n % 2) - 1)
    print(F[-1])
else:
    print(0)
    print(0)