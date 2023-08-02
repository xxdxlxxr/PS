def factorial(N):
    if N == 1:
        return 1

    return N * factorial(N - 1)

n, k = map(int, input().split())

print(1 if k == 1 or n == k else factorial(n - 1) // factorial(k - 1) // factorial(n - k))