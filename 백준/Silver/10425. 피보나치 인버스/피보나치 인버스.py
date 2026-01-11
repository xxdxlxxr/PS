def fibonacci(n):
    tmp = [0, 1]

    while 1:
        next = tmp[-1] + tmp[-2]

        if next > n:
            break

        tmp.append(next)

    return len(tmp) - 1

for _ in range(int(input())):
    print(fibonacci(int(input())))