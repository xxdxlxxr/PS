for i in range(1000, 10000):
    tmp, notation = 3 * [0], [16, 12, 10]

    for j in range(3):
        num = i

        while num != 0:
            tmp[j] += num % notation[j]
            num //= notation[j]

    if tmp[0] == tmp[1] == tmp[2]:
        print(i)