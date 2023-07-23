def solution(myString, pat):
    answer = 0
    
    for i in range(len(myString) - len(pat) + 1):
        answer += pat == myString[i:i + len(pat)]
    
    return answer