def solution(arr, k):
    return [k * num if k % 2 else num + k for num in arr]