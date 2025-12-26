N, M, S, P, i, cnt, answer = int(input()), int(input()), input(), 'IOI', 0, 0, 0

while i + 1 < M:
    if S[i : i + 3] == P:
        i += 2
        cnt += 1

        if cnt == N:
            answer += 1
            cnt -= 1
    else:
        i += 1
        cnt = 0

print(answer)