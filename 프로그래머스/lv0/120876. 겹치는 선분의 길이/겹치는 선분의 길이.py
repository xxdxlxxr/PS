def solution(lines):
    tmp1, tmp2, tmp3, answer = function(lines[0], lines[1]), function(lines[0], lines[2]), function(lines[1], lines[2]), []
    
    for tmp in [tmp1, tmp2, tmp3]:
        for i in range(tmp[0] + 1, tmp[1] + 1):
            if not i in answer:
                answer.append(i)
    
    return len(answer)

    
def function(x, y):
    if min(x[1], y[1]) - max(x[0], y[0]) > 0:
        return [max(x[0], y[0]), min(x[1], y[1])]
    else:
        return [0, 0]