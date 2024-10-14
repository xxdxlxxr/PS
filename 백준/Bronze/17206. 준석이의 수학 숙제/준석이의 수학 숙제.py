input()
check, tmp = 80001 * [0], 0

for i in range(80001):
    if i % 3 == 0 or i % 7 == 0:
        tmp += i

    check[i] = tmp

for N in map(int, input().split()):
    print(check[N])