def solution(code):
    mode, answer = 0, ''
    
    for i in range(len(code)):
        if code[i] == '1':
            mode = not(mode)
        elif mode:
            if i % 2:
                answer += code[i]
        else:
            if not i % 2:
                answer += code[i]
    
    if answer == '':
        return 'EMPTY'
    else:
        return answer