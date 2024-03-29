N = int(input())
A = list(map(int, input().split()))
stack, answer = [], []

for i in range(N):
    while stack:
        if stack[-1][1] > A[i]:
            answer.append(stack[-1][0] + 1)
            break
        else:
            stack.pop()

    if not stack:
        answer.append(0)

    stack.append([i, A[i]])

print(*answer)
