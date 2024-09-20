K, S = 1, input()

for i in range(len(S) - 1):
    if S[i] >= S[i + 1]:
        K += 1

print(K)