def is_prime(n):
    i = 5

    if n % 2 == 0:
        return n == 2

    if n % 3 == 0:
        return n == 3

    while i * i <= n:
        if n % i == 0:
            return False

        i += 2

    return n != 1

sum = 0

for i in range(int(input()), int(input()) + 1):
    if is_prime(i):
        if sum == 0:
            minimum = i

        sum += i

if sum:
    print(sum)
    print(minimum)
else:
    print(-1)