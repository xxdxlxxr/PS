def func(x):
    return int(x) + (x >= int(x) + 0.5)

n = int(input())

if n:
    tmp = []

    for _ in range(n):
        tmp.append(int(input()))
        n_tmp = func(0.15 * n)

    tmp.sort()

    if n_tmp > 0:
        print(func(sum(tmp[n_tmp:-n_tmp]) / len(tmp[n_tmp:-n_tmp])))
    else:
        print(func(sum(tmp) / len(tmp)))
else:
    print(0)