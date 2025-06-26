N = int(input())
N = int(N ** .5) + (N ** .5 != int(N ** .5))

print((N + 2) * 'x')

for _ in range(N):
    print('x' + N * '.' + 'x')

print((N + 2) * 'x')