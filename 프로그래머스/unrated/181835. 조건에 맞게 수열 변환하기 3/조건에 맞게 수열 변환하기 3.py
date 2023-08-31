def solution(arr, k):
    return [k * num for num in arr] if k % 2 else [num + k for num in arr]