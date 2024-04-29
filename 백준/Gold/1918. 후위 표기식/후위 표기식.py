stack, answer = [], ''

for char in input():
    if char.isalpha():
        answer += char
    elif char == '(':
        stack.append(char)
    elif char == ')':
        while stack and stack[-1] != '(':
            answer += stack.pop()

        stack.pop()
    elif char in '*/':
        while stack and stack[-1] in '*/':
            answer += stack.pop()

        stack.append(char)
    else:
        while stack and stack[-1] != '(':
            answer += stack.pop()

        stack.append(char)
        
while stack:
    answer += stack.pop()

print(answer)