import sys

S = set()

for _ in range(int(input())):
    command = sys.stdin.readline().split()

    if command[0] == 'add':
        S.add(command[1])
    elif command[0] == 'remove':
        if command[1] in S:
            S.remove(command[1])
    elif command[0] == 'check':
        print(int(command[1] in S))
    elif command[0] == 'toggle':
        if command[1] in S:
            S.remove(command[1])
        else:
            S.add(command[1])
    elif command == ['all']:
        S = set(map(str, range(1, 21)))
    else:
        S = set()