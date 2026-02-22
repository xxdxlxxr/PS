X, Y, W, S = map(int, input().split())
answer = 0

if 2 * W <= S:
    print((X + Y) * W)
else:
    answer = S * min(X, Y)
    tmp = abs(X - Y)

    if W > S:
        if tmp % 2 == 0:
            answer += S * tmp
        else:
            answer += (tmp - 1) * S + W
    else:
        answer += W * tmp
        
    print(answer)