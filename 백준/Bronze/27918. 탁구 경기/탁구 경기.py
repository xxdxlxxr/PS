answer = [0, 0]

for _ in range(int(input())):
    if input() == 'D':
        answer[0] += 1
    else:
        answer[1] += 1

    if abs(answer[0] - answer[1]) == 2:
        break

print(answer[0], ':', answer[1], sep = '')