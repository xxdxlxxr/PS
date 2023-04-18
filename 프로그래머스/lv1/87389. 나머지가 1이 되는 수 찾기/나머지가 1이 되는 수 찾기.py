def solution(n):
    return next(i for i in range(2, n) if not (n - 1) % i)