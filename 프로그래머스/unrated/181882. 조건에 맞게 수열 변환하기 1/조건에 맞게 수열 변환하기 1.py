def solution(arr):
    return [arr[i] // ((arr[i] >= 50 and not (arr[i] % 2)) + 1) * ((arr[i] < 50 and arr[i] % 2) + 1) for i in range(len(arr))]