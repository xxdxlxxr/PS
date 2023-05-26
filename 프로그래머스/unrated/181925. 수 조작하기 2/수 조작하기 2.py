def solution(numLog):
    length, answer = len(numLog), ''
    
    for i in range(length - 1):
        tmp = numLog[i + 1] - numLog[i]
        
        if tmp == 1: answer += 'w'
        elif tmp == -1: answer += 's'
        elif tmp == 10: answer += 'd'
        else: answer += 'a'
    
    return answer