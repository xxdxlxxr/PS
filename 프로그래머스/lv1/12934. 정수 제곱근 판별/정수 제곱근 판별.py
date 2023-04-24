def solution(n):
    if n ** .5 == int(n ** .5):
        return (n ** .5 + 1) ** 2
    else:
        return -1