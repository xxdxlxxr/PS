T, D, M = map(int, input().split())
now, answer = 0, 'N'

for _ in range(M):
    tmp = int(input())

    if tmp >= T + now:
        answer = 'Y'
        break

    now = tmp

if D >= T + now:
    answer = 'Y'

print(answer)