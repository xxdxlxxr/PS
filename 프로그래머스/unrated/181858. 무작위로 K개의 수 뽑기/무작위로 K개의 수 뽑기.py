def solution(arr, k):
    answer, cnt = [], 0
    
    for num in arr:
        if not num in answer:
            answer.append(num)
            cnt += 1
            
        if cnt == k:
            break
    
    return answer + (k - cnt) * [-1]