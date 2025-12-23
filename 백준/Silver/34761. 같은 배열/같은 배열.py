N, A, B, check = int(input()), list(map(int, input().split())), list(map(int, input().split())), 1

if A[:N] != B[:N]:
    check = 0
else:
    set_A = set(A)

    for i in range(N, 2 * N):
        tmp = B[i]

        if tmp not in set_A:
            check = 0
            break

        set_A.add(tmp)

print(['NO', 'YES'][check])