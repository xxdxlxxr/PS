def solution(s):
    answer = []
    
    for alpha in set(s):
        if s.count(alpha) == 1:
            answer.append(alpha)
            
    return ''.join(sorted(answer))