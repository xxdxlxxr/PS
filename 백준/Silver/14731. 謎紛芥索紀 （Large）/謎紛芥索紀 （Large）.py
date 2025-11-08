def function(a, b, c):
    if b < 0:
        return 0

    result = 1
    cur = a

    while b:
        if b & 1:
            result = result * cur % c

        cur = cur * cur % c
        b //=2

    return result

tmp = int(1e9 + 7)
answer = 0

for _ in range(int(input())):
    C, K = map(int, input().split())
    answer += C * K * function(2, K - 1, tmp)

print (answer % tmp)