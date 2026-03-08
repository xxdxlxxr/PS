def function1(x):
    i = 0

    while pow(i, 2) < x:
        i += 1

    return i

def function2(a, b):
    if (a - 1) * a > b:
        return 4 * a - 6
    else:
        return 4 * a - 4

N = int(input())
print(0 if N == 0 else 4 if N == 1 else function2(function1(N), N))