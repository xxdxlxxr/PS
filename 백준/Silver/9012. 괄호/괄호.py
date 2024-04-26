for _ in range(int(input())):
    stack = []

    for char in input():
        if char == '(':
            stack.append(char)
        else:
            if stack:
                stack.pop()
            else:
                print('NO')
                break
    else:
        if stack:
            print('NO')
        else:
            print('YES')