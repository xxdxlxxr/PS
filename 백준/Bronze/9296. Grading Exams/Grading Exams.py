for i in range(int(input())):
    L, answer, responses, cnt = int(input()), input(), input(), 0

    for j in range(L):
        cnt += answer[j] != responses[j]

    print(f'Case {i + 1}: {cnt}')