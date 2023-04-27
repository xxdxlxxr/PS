def solution(s):
    arr, answer = 26 * [0], []
    
    for i in range(len(s)):
        if s[i] in s[:i]:
            answer.append(list(reversed(s[:i])).index(s[i]) + 1)
        else:
            answer.append(-1)
    
    return answer