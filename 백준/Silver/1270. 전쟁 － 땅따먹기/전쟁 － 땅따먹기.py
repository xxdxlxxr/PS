for _ in range(int(input())):
    numbers = list(map(int, input().split()))
    tmp, key, val = dict(), 0, 0

    for i in range(1, len(numbers)):
        if numbers[i] not in tmp:
            tmp[numbers[i]] = 1
        else:
            tmp[numbers[i]] += 1

        if tmp[numbers[i]] > val:
            val = tmp[numbers[i]]
            key = numbers[i]

    print(key if val > numbers[0] / 2 else 'SYJKGW')