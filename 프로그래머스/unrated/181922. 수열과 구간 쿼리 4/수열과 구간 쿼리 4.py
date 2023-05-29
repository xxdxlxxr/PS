def solution(arr, queries):
    for s, e, k in queries:
        for i in range(e - s + 1):
            arr[s + i] += (s + i) % k == 0
    
    return arr