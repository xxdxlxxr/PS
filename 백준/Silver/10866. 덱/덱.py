import sys

input = sys.stdin.readline
A = []

for i in range(int(input())):
    command = input().rstrip()

    if " " in command:
        a,b = command.split()

        if a == 'push_front':
            A.insert(0,b)
        elif a == 'push_back':
            A.append(b)
    elif "pop_front" == command: 
        if len(A) == 0:
            print(-1)
        else:
            print(A.pop(0))
    elif "pop_back" == command: 
        if len(A) == 0:
            print(-1)
        else:
            print(A.pop(-1))    
    elif 'size' == command:
        print(len(A))
    elif 'empty' == command:
        if len(A) == 0:
            print(1)
        else:
            print(0)
    elif 'front' == command:
        if len(A) == 0:
            print(-1)
        else:
            print(A[0])
    elif 'back' == command:
        if len(A) == 0:
            print(-1)
        else:
            print(A[-1])