N, stack, turn = int(input()), [], 1

for student in map(int, input().split()):
    stack.append(student)

    while stack and stack[-1] == turn:
        stack.pop()
        turn += 1

print('Sad' if stack else 'Nice')