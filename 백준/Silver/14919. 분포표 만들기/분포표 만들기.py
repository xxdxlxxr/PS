m = int(input())
A = list(map(float, input().split()))
answer = [0] * m

for a in A:
    for i in range(m):
        if i / m <= a < (i + 1) / m:
            answer[i] += 1
            break

print(*answer)