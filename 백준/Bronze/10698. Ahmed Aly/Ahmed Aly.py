for i in range(int(input())):
    equation = input().split('=')
    print(f'Case {i + 1}:', 'YES' if eval(equation[0]) == int(equation[1]) else 'NO')