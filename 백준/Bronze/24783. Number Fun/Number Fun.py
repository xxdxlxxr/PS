import sys

for _ in range(int(input())):
    a, b, c = map(int, sys.stdin.readline().split())
    answer = 0

    for operator in '+-*/':
        if eval(str(max(a, b)) + operator + str(min(a, b))) == c:
            answer = 1
            break

    print('Possible' if answer else 'Impossible')