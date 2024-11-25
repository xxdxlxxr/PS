for _ in range(int(input())):
    expression = input().split()
    answer = expression[0]

    for op in expression[1:]:
        answer = str(eval(answer + ['*3', '+5', '-7']['@%#'.index(op)]))

    print('%.2f' % float(answer))