answer = 0

for _ in range(int(input())):
    stack, tmp = [], list(input())

    for i in tmp:
        if not len(stack):
            stack.append(i)
        elif stack[-1] == i:
            stack.pop(-1)
        else:
            stack.append(i)

    if not len(stack):
        answer += 1 

print(answer)