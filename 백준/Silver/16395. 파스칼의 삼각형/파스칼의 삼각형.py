def factorial(N):
    if N == 1:
        return 1

    return N * factorial(N - 1)

n, k = map(int, input().split())

if k == 1 or n == k:
    print(1)
else:
    print(factorial(n - 1) // factorial(k - 1) // factorial(n - k))