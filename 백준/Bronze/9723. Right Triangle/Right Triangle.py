for i in range(int(input())):
    abc = sorted(list(map(int, input().split())))

    if abc[0] ** 2 + abc[1] ** 2 == abc[2] ** 2:
        answer = 'YES'
    else:
        answer = 'NO'

    print(f'Case #{i + 1}: {answer}')