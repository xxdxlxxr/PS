def solution(food):
    answer = ''
    
    for i in range(1, len(food)):
        answer += food[i] // 2 * str(i)
    
    return answer + '0' + ''.join(reversed(answer))