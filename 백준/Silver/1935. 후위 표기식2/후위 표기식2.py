N, expression, stack = int(input()), input(), []
value = {chr(ord('A') + i): input() for i in range(N)}

for char in expression:
    if char.isalpha():
        stack.append(value[char])
    else:
        y, x = stack.pop(), stack.pop()
        stack.append(str(eval(x + char + y)))
        
print('%.2f' % float(stack.pop()))