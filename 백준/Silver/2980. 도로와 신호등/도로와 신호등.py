N, L = map(int,input().split())
tmp, answer = 0, 0

for _ in range(N):
    D, R, G = map(int,input().split())
    answer += D - tmp
    tmp = D

    if answer % (R + G) <= R:
        answer += R - answer % (R + G)

print(answer + L - tmp)