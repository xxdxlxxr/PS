N, A, state, answer = int(input()), list(map(int, input().split())), 0, 1

for i in range(N - 1):
    if A[i] < A[i + 1]:
        if state:
            answer = 0
            break
    elif A[i] == A[i + 1]:
        answer = 0
        break
    else:
        state = 1

print('YES' if answer else 'NO')