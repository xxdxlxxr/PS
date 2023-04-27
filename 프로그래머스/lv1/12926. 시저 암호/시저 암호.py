def solution(s, n):
    answer = ''
    
    for alpha in s:
        if alpha.isupper():
            answer += chr(((ord(alpha) + n - 65) % 26 + 65))
        elif alpha.islower():
            answer += chr(((ord(alpha) + n - 97) % 26 + 97))
        else:
            answer += ' '
    
    return answer