for _ in range(int(input())):
    expression = input().split()

    print('correct' if eval(''.join(expression[:3])) == int(expression[-1]) else 'wrong answer')