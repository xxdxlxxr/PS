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

N, answer = int(input()), 0

for num in map(int, input().split()):
    if is_prime(num):
        answer += 1

print(answer)