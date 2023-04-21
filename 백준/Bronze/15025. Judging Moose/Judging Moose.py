l, r = map(int, input().split())

if not l + r:
    print('Not a moose')
else:
    print('Even' if l == r else 'Odd', end = ' ')
    print(2 * max(l, r))