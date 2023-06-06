def solution(arr):
    i, stk = 0, []
    
    while i < len(arr):
        if not stk or stk[-1] < arr[i]:
            stk.append(arr[i])
            i += 1
        else:
            stk.pop()
                
    return stk