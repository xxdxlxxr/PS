print('n e')
print('- -----------')
print('0 1')

for i in range(1, 10):
    sum = 1

    for j in range(1, i + 1):
        tmp = 1

        for num in range(1, j + 1):
            tmp *= num

        sum += 1 / tmp

    print(i, int(sum) if i == 1 else sum if i == 2 else '%.9f'%sum)