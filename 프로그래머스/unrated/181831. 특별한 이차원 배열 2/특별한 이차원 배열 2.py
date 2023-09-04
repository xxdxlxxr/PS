def solution(arr):
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i][j] != arr[j][i]:
                return 0
            
    return 1