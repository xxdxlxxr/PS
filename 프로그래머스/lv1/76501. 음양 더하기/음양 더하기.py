def solution(absolutes, signs):
    answer = 0
    
    for i in range(len(absolutes)):
        answer += absolutes[i] * (2 * signs[i] - 1)
    
    return answer