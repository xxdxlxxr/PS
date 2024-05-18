for _ in range(int(input())):
    m, n = map(int, input().split())
    L, answer = [[] for _ in range(n)], 0

    for i in range(m):
        line = list(map(int, input().split()))

        for j in range(n):
            if line[j]:
                L[j].append(m - i)
                
    for l in L:
        size = len(l)
        answer += sum(l) - size * (size + 1) // 2

    print(answer)