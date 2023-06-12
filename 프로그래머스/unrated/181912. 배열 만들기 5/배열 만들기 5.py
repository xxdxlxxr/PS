def solution(intStrs, k, s, l):
    answer = []
    
    for intStr in intStrs:
        tmp = int(intStr[s:s + l])
        
        if tmp > k:
            answer.append(tmp)
    
    return answer