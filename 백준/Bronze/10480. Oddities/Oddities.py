for _ in range(int(input())):
    x = int(input())

    print('{} is {}'.format(x, (x % 2) * 'odd' + (x % 2 == 0) * 'even'))