for i in range(1, 12001):
    a, op, b = input().split()

    if op == 'E':
        break

    print(f'Case {i}: {str(eval(a+op+b)).lower()}')