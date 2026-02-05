def DFS(s):
    global answer

    if len(s) == 1:
        answer = 'AKARAKA'
        return
    
    else:
        if s != s[::-1]:
            return
        else:
            N = len(s) // 2
            DFS(s[:N])
            DFS(s[-N:])

S, answer = input(), 'IPSELENTI'
DFS(S)
print(answer)