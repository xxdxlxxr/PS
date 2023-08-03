def solution(arr, flag):
    answer = []
    
    for i in range(len(arr)):
        if flag[i]:
            answer += 2 * arr[i] * [arr[i]]
        else:
            answer = answer[:-arr[i]]
    
    return answer