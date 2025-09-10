S, answer = input(), 0

for i in range(len(S)):
    answer += S[i] == 'KOREA'[answer % 5]

print(answer)