while 1:
    a, b, c = map(int, input().split())

    if a == 0:
        break

    print('Invalid' if sum((a, b, c)) <= 2 * max((a, b, c)) else 'Equilateral' if a == b == c else 'Isosceles' if a == b or b == c or c == a else 'Scalene')