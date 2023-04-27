S, answer = input(), 26 * [-1]

for i in range(len(S)):
    answer[ord(S[i]) - 97] = S.index(S[i])

print(*answer)