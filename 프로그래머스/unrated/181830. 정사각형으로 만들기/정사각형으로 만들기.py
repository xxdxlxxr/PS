def solution(arr):
    if len(arr) > len(arr[0]):
        arr = [nums + (len(arr) - len(arr[0])) * [0] for nums in arr]
    elif len(arr) < len(arr[0]):
        arr += (len(arr[0]) - len(arr)) * [len(arr[0]) * [0]]
    
    return arr