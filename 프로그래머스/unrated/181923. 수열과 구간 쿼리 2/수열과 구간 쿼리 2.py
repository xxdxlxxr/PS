def solution(arr, queries):
    answer = []
    
    for s, e, k in queries:
        tmp = sorted(arr[s:e + 1])
        answer.append(next((x for x in tmp if x > k), -1))
                    
    return answer