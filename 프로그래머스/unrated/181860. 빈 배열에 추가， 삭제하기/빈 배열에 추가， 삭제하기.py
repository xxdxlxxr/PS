def solution(arr, flag):
    X = []
    
    for i, num in enumerate(arr):
        if flag[i]:
            X += 2 * num * [num]
        else:
            X = X[:-num]
    
    return X