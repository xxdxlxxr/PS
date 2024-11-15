answer, tmp = '', 0

for _ in range(7):
    S = input().split()
    S[1] = int(S[1])

    if S[1] > tmp:
        answer = S[0]
        tmp = S[1]

print(answer)