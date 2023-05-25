def solution(n, control):
    for alpha in control:
        if alpha == 'w': n += 1
        elif alpha == 's': n -= 1
        elif alpha == 'd': n += 10
        else: n -= 10
    
    return n