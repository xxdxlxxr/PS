def solution(a, d, included):
    sum = 0
    
    for i in range(len(included)):
        if included[i]:
            sum += i
    
    return included.count(1) * a + sum * d