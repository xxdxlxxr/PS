A, B = map(int, input().split())
D = A ** 2 - B

if D:
    print(-A - int(D ** .5), -A + int(D ** .5))
else:
    print(-A)