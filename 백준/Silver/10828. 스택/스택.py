import sys

stack = []

for _ in range(int(input())):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        stack.append(command[1])
    elif command[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        print(int(stack == []))
    else:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])