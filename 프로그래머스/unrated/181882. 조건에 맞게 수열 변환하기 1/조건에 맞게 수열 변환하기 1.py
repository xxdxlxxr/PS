def solution(arr):
    return [num // ((num >= 50 and not (num % 2)) + 1) * ((num < 50 and num % 2) + 1) for num in arr]