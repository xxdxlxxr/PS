def solution(arr, n):
    return [num + int(not i % 2) * n for i, num in enumerate(arr)] if len(arr) % 2 else [num + i % 2 * n for i, num in enumerate(arr)]