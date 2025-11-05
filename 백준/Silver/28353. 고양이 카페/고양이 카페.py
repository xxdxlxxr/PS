N, K = map(int, input().split())
w = list(sorted(map(int, input().split())))
tmp_1, tmp_2, answer = 0, N - 1, 0

while tmp_1 < tmp_2:
    if w[tmp_1] + w[tmp_2] <= K:
        tmp_1 += 1
        tmp_2 -= 1
        answer += 1
    else:
        tmp_2 -= 1

print(answer)