import sys

queue = []

for _ in range(int(input())):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        queue.insert(0, command[1])
    elif command[0] == 'pop':
        print(queue.pop() if queue else -1)
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        print(int(len(queue) == 0))
    elif command[0] == 'front':
        print(queue[-1] if queue else -1)
    else:
        print(queue[0] if queue else -1)