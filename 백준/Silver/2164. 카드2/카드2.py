N = int(input())
a = 2

while True:
    if N == 1 or N == 2:
        print(N)
        break

    a *= 2

    if a >= N:
        print((N - (a // 2)) * 2)
        break