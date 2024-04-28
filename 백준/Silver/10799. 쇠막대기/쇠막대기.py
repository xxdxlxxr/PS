s, stack, answer = input(), [], 0

for i in range(len(s)):
    if s[i] == '(':
        stack.append('(')
    elif s[i - 1] == '(':
        stack.pop()
        answer += len(stack)
    else:
        stack.pop()
        answer += 1
        
print(answer)