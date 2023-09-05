def solution(arr):
    row, col = len(arr), len(arr[0])
    
    return [nums + (row - col) * [0] for nums in arr] if row > col else arr + (col - row) * [col * [0]] if row < col else arr