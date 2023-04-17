def solution(numbers):
    answer = 0
    
    for i in range(10):
        if not numbers.count(i):
            answer += i
    
    return answer