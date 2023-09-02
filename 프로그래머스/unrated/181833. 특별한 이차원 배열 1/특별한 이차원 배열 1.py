def solution(n):
    answer = [n * [0] for _ in range(n)]
    
    for i in range(n):
        answer[i][i] = 1
    
    return answer