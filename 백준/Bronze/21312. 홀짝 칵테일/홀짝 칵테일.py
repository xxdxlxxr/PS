ABC = list(map(int, input().split()))
answer, cnt = 1, 0

for num in ABC:
    if num % 2:
        answer *= num
        cnt += 1

if cnt == 0:
    answer = ABC[0] * ABC[1] * ABC[2]

print(answer)