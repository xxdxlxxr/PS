N, S, cnt, answer = int(input()), list(input()), 1, 0

for i in range(N - 1):
    if abs(ord(S[i]) - ord(S[i + 1])) == 1:
        cnt += 1
    else:
        cnt = 1

    if cnt == 5:
        answer = 1
        break

print(['NO', 'YES'][answer])