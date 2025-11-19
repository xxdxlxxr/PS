N = input()

if '0' not in N:
    print(-1)
else:
    total = 0

    for i in range(len(N)):
        total += int(N[i])

    if total % 3 != 0:
        print(-1)
    else:
        print(''.join(sorted(N, reverse=True)))