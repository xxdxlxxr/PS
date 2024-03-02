order = 1

while 1:
    n = int(input())

    if n == 0:
        break

    n *= 3
    odd_or_even = 'odd' if n % 2 else 'even'
    n = (n + 1) // 2
    n *= 3
    n = (n + 1) // 9

    print(str(order) + '.', odd_or_even, n)

    order += 1