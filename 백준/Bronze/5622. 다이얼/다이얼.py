arr, cnt = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ'], 0

for alpha in input():
    for alphas in arr:
        if alpha in alphas:
            cnt += arr.index(alphas) + 3

print(cnt)