def solution(a, d, included):
    answer = 0
    
    for i in range(len(included)):
        answer += included[i] * (a + i * d)
    
    return answer