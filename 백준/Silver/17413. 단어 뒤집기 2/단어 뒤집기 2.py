stack, state, S, answer = [], 0, input().strip() + ' ', ''

for char in S:
    if char == '<':
        for _ in range(len(stack)):
            answer += stack.pop()

        state = 1

    stack.append(char)

    if char == '>':
        for _ in range(len(stack)):
            answer += stack.pop(0)

        state = 0
    elif char == ' ' and not state:
        stack.pop()

        for _ in range(len(stack)):
            answer += stack.pop()

        answer += char

print(answer)