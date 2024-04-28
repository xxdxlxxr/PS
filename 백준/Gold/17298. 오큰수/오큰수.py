N, A, stack = int(input()), list(map(int, input().split())), []
answer = N * [-1]

for i in range(N):
    while stack and A[i] > A[stack[-1]]:
        answer[stack[-1]] = A[i]
        stack.pop()

    stack.append(i)

print(*answer)