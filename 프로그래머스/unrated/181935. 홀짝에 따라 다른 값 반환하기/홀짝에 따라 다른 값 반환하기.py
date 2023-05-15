def solution(n):
    if n % 2:
        return ((n + 1) // 2) ** 2
    else:
        return sum([i ** 2 for i in list(range(n + 1))[2::2]])