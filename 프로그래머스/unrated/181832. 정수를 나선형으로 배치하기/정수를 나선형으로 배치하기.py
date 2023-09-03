def solution(n):
    answer, cnt, x, y, tmp, d = [[0 for _ in range(n)] for _ in range(n)], 0, -1, 0, [n], [[0, 1], [1, 0], [0, -1], [-1, 0]]
    
    while n > 1:
        n -= 1
        tmp += [n, n]
        
    for i in range(len(tmp)):
        for j in range(tmp[i]):
            y += d[i % 4][0]
            x += d[i % 4][1]
            cnt += 1
            answer[y][x] = cnt
    
    return answer