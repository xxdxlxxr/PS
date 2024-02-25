for i in range(int(input())):
    sum = int(input())

    print(f'Case {i + 1}:')

    for j in range(1, 7):
        for k in range(j, 7):
            if j + k == sum:
                print(f'({j},{k})')