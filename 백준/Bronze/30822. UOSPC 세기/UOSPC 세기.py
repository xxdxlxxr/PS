n, S, cnt = int(input()), input(), 5 * [0]

for i in range(n):
    if S[i] in 'uospc':
        cnt['uospc'.index(S[i])] += 1

print(min(cnt))