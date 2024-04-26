left, right = list(input()), []

for _ in range(int(input())):
    command = input().split()

    if command[0] == 'L' and left:
        right.append(left.pop())
    elif command[0] == 'D' and right:
        left.append(right.pop())
    elif command[0] == 'B' and left:
        left.pop()
    elif command[0] == 'P':
        left.append(command[1])

print(''.join(left + right[::-1]))