def solution(strArr):
    cnt = 30 * [0]
    
    for str in strArr:
        cnt[len(str) - 1] += 1
    
    return max(cnt)