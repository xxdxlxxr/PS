def solution(s):
    s, answer, cnt = sorted(s), [], 0
    s.append(' ')
    
    for i in range(1, len(s)):
        if s[i - 1] == s[i]:
            cnt += 1
        else:
            if not cnt:
                answer.append(s[i - 1])
            
            cnt = 0
            
    return ''.join(answer)