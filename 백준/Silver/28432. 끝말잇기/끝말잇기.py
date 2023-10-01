S, A = [input() for _ in range(int(input()))], [input() for _ in range(int(input()))]

if len(S) == 1:
    print(A[0])
elif S[0] == '?':
    for string in A:
        if string not in S and string[-1] == S[1][0]:
            print(string)
            break
elif S[-1] == '?':
    for string in A:
        if string not in S and string[0] == S[-2][-1]:
            print(string)
            break
else:
    i = S.index('?')

    for string in A:
        if string not in S and string[0] == S[i - 1][-1] and string[-1] == S[i + 1][0]:
            print(string)
            break