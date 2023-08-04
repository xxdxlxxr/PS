def solution(arr):
    answer = []
    
    for i, num in enumerate(arr):
        if not answer:
            answer = [num]
            continue
            
        if answer[-1] == num:
            answer.pop()
        else:
            answer.append(num)
    
    return answer if answer else [-1]