def function(a, b, c, d):
    tmp = c

    while tmp <= a * b:
        if (tmp - c) % a == 0 and (tmp - d) % b == 0:
            return tmp

        tmp += a

    return -1

for _ in range(int(input())):
    M, N, x, y = map(int, input().split())
    print(function(M, N, x, y))