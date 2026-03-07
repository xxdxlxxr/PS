import sys

N, M = list(map(int, input().split()))
S, answer = list(map(int, input().split())), sys.maxsize

for i in range(1, 1002):
    if i in S:
        continue

    for j in range(1, 1002):
        if j in S:
            continue

        for k in range(1, 1002):
            if k in S:
                continue
            
            q = (i * j * k)

            if abs(N - q) < answer:
                answer = abs(N - q)

            if N + 1 < q:
                break

print(answer)