N, A, cnt, stack = int(input()), list(map(int, input().split())), 1000001 * [0], []
answer = N * [-1]

for num in A:
    cnt[num] += 1
    
for i in range(N):
    while stack and cnt[A[stack[-1]]] < cnt[A[i]]:
        answer[stack.pop()] = A[i]

    stack.append(i)

print(*answer)