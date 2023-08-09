def solution(arr, n):
    return [num + n if i % 2 == (len(arr) + 1) % 2 else num for i, num in enumerate(arr)]