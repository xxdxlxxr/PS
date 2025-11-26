def func(n):
    tmp = []

    for i in range(2, n + 1):
        cnt = 0

        while n % i == 0:
            cnt += 1
            n = n // i

        if cnt:
            tmp.append([i, cnt])

    for nums in tmp:
        print(*nums)

for _ in range(int(input())):
    func(int(input()))