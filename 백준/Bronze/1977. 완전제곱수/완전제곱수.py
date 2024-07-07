M, N = int(input()), int(input())
tmp = [i for i in range(M, N + 1) if i ** .5 == int(i ** .5)]

if tmp:
    print(sum(tmp))
    print(min(tmp))
else:
    print(-1)