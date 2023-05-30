def solution(l, r):
    tmp, answer = [], []
    
    for i in range(1, 2 ** 7 + 1):
        tmp.append(5 * int(bin(i)[2:]))
    
    for num in tmp:
        if l <= num <= r:
            answer.append(num)
    
    if answer:
        return answer
    else:
        return [-1]