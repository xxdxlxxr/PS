stack, answer, cnt = [], [], 1

for _ in range(int(input())):
    num = int(input())

    for i in range(cnt, num + 1):
        stack.append(i)
        answer.append('+')
        cnt += 1

    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    else:
        print('NO')
        break
else:
    for char in answer:
        print(char)