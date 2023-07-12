days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for _ in range(int(input())):
    x, y = map(int, input().split())
    answer = ['Yes', 'Yes']

    if x > 23 or y > 59:
        answer = ['No', 'No']
    elif x > 12 or not x or not y:
        answer[1] = 'No'
    elif y > days[x - 1]:
        answer[1] = 'No'

    print(*answer)